from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import *

def get_file_type(filename):
    name = filename.lower()

    if name.endswith('.pdf'):
        return 'PDF'
    elif name.endswith('.docx'):
        return 'DOCX'
    elif name.endswith('.doc'):
        return 'DOC'
    elif name.endswith('.txt'):
        return 'TXT'
    elif name.endswith(('.jpg', '.jpeg')):
        return 'JPG'
    elif name.endswith('.png'):
        return 'PNG'
    elif name.endswith('.gif'):
        return 'GIF'
    else:
        return 'OTHER'

def filenest(request):
    user = Users.objects.get(id=request.user.id)
    files = Files.objects.filter(owner=user)
    folders = Folders.objects.filter(owner=user)

    file_count = files.count()
    folder_count = folders.count()

    documents = 0
    pdfs = 0
    images = 0
    others = 0

    for file in files:
        name = file.file_name.lower()

        if name.endswith('.pdf'):
            pdfs += file.file_size
        elif name.endswith('.doc') or name.endswith('.docx') or name.endswith('.txt'):
            documents += file.file_size
        elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png') or name.endswith('.gif'):
            images += file.file_size
        else:
            others += file.file_size

    total_size = documents + pdfs + images + others

    storage_limit = 10 * 1024 * 1024 * 1024

    percentage = (total_size / storage_limit) * 100

    def size(size):
        if size < 1024:
            return str(size) + " Bytes"
        elif size < 1024 * 1024:
            return str(round(size / 1024, 2)) + " KB"
        elif size < 1024 * 1024 * 1024:
            return str(round(size / (1024 * 1024), 2)) + " MB"
        else:
            return str(round(size / (1024 * 1024 * 1024), 2)) + " GB"

    storage = size(total_size)
    documents = size(documents)
    pdfs = size(pdfs)
    images = size(images)
    others = size(others)

    recent_files = files.order_by('-uploaded_at')[:5]

    d = {
        'file_count': file_count,
        'folder_count': folder_count,
        'storage': storage,
        'percentage': round(percentage, 1),
        'documents': documents,
        'pdfs': pdfs,
        'images': images,
        'others': others,
        'recent_files': recent_files
    }

    return render(request, 'filenest.html', d)


def upload_file(request):
    user = Users.objects.get(id=request.user.id)

    if request.method == 'POST':
        files = request.FILES.getlist('file')

        for uploaded_file in files:
            file = Files()

            file.owner = user
            file.file = uploaded_file
            file.file_name = uploaded_file.name
            file.description = request.POST.get('description', '')
            file.file_size = uploaded_file.size
            file.file_type = get_file_type(uploaded_file.name)
            folder = request.POST.get('folder')

            if folder:
                file.folder_id = folder

            file.save()

        return redirect('/filenest')

    else:
        f = FileForm()
        f.fields['folder'].queryset = Folders.objects.filter(owner=user)
        d = {'form': f}

        return render(request, 'fileupload.html', d)

def edit_file(request, id):
    file = Files.objects.get(id=id)

    if request.method == 'POST':
        file.file_name = request.POST['file_name']
        file.description = request.POST['description']
        file.save()

        return redirect('/filenest')

    else:
        d = {'file': file}
        return render(request, 'editfile.html', d)


def file_details(request, id):
    file = Files.objects.get(id=id)
    file.size_mb = round(file.file_size / (1024 * 1024), 2)
    d = {'file': file}
    return render(request, 'filedetails.html', d)


def download_file(request, id):
    file = Files.objects.get(id=id)

    return FileResponse(file.file.open('rb'), as_attachment=True, filename=file.file_name)

def delete_file(request, id):
    file = Files.objects.get(id=id)

    file.file.delete()
    file.delete()

    return redirect('/filenest')


def preview_file(request, id):
    file = Files.objects.get(id=id)

    return redirect(file.file.url)


def show_files(request):
    user = Users.objects.get(id=request.user.id)

    files = Files.objects.filter(owner=user).exclude(trash__isnull=False)

    file_type = request.GET.get('type')
    sort = request.GET.get('sort')

    if file_type == 'pdf':
        files = files.filter(file_type='PDF')

    elif file_type == 'document':
        files = files.filter(file_type__in=['DOC', 'DOCX', 'TXT'])

    elif file_type == 'image':
        files = files.filter(file_type__in=['JPG', 'PNG', 'GIF'])

    elif file_type == 'other':
        files = files.filter(file_type='OTHER')

    if sort == 'name':
        files = files.order_by('file_name')

    elif sort == 'time':
        files = files.order_by('-uploaded_at')

    folders = Folders.objects.filter(owner=user)

    users = Users.objects.exclude(id=user.id)

    for file in files:
        file.size_mb = round(file.file_size / (1024 * 1024),2)

    d = {'files': files, 'folders': folders, 'users': users}
    return render(request, 'files.html', d)


def move_file(request, id):
    file = Files.objects.get(id=id, owner=request.user)

    folders = Folders.objects.filter(owner=request.user)
    if request.method == 'POST':
        folder_id = request.POST['folder']

        folder = Folders.objects.get(id=folder_id, owner=request.user)
        file.folder = folder
        file.save()

        return redirect('/files')

    d = {'file': file, 'folders': folders}
    return render(request, 'movefile.html', d)



