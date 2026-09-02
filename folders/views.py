from django.shortcuts import render,redirect
from .models import *
from account.models import Users
from files.models import Files

# Create your views here.
def folders(request):
    user = Users.objects.get(id=request.user.id)
    folders = Folders.objects.filter(owner=user,parent=None)
    d = {'folders': folders}
    return render(request, 'folders.html', d)

def create_folder(request):
    if request.method == 'POST':
        f = FolderForm(request.POST)
        if f.is_valid():
            folder = f.save(commit=False)
            user = Users.objects.get(id=request.user.id)
            folder.owner = user
            folder.save()
            return redirect('/folders')
    else:
        f = FolderForm()
        d = {'form': f}
        return render(request, 'createfolder.html', d)

def rename_folder(request, id):
    folder = Folders.objects.get(id=id)
    if request.method == 'POST':
        folder.folder_name = request.POST['folder_name']
        folder.save()
        return redirect('/folders')
    else:
        d = {'folder': folder}
        return render(request, 'renamefolder.html', d)

def delete_folder(request, id):
    folder = Folders.objects.get(id=id)
    folder.delete()
    return redirect('/folders')

def open_folder(request, id):
    user = Users.objects.get(id=request.user.id)
    folder = Folders.objects.get(id=id, owner=user)
    subfolders = Folders.objects.filter(parent=folder, owner=user)
    files = Files.objects.filter(folder=folder, owner=user)
    all_folders = Folders.objects.filter(owner=user)
    for file in files:
        file.size_mb = round(file.file_size / (1024 * 1024), 2)
    d = {
        'folder': folder,
        'folders': subfolders,
        'files': files,
        'all_folders': all_folders
    }
    return render(request, 'openfolder.html', d)

def create_subfolder(request, id):
    parent = Folders.objects.get(id=id)
    if request.method == 'POST':
        folder = Folders()
        folder.folder_name = request.POST['folder_name']
        folder.owner = Users.objects.get(id=request.user.id)
        folder.parent = parent
        folder.save()
        return redirect('/open_folder/' + str(parent.id))
    else:
        d = {'parent': parent}
        return render(request, 'createsubfolder.html', d)

def move_file(request, id):
    user = Users.objects.get(id=request.user.id)
    file = Files.objects.get(id=id, owner=user)
    folders = Folders.objects.filter(owner=user)
    if request.method == 'POST':
        folder_id = request.POST['folder']
        folder = Folders.objects.get(id=folder_id, owner=user)
        file.folder = folder
        file.save()
        return redirect('/open_folder/' + str(folder.id))
    else:
        d = {'file': file, 'folders': folders}
        return render(request, 'movefile.html', d)

def move_folder(request, id):
    folder = Folders.objects.get(id=id)
    folders = Folders.objects.filter(owner=request.user).exclude(id=id)

    if request.method == 'POST':
        parent_id = request.POST.get('parent')
        if parent_id:
            parent = Folders.objects.get(id=parent_id)
            folder.parent = parent
        else:
            folder.parent = None
        folder.save()
        return redirect('/folders')
    
    else:
        d = {'folder': folder,'folders': folders}
        return render(request, 'movefolder.html', d)