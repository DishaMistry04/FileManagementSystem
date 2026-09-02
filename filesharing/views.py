from django.shortcuts import render, redirect
from .models import FileShare
from files.models import Files
from account.models import Users

def shared_files(request):
    user = Users.objects.get(id=request.user.id)
    shares = FileShare.objects.filter(shared_with=user)
    d = {'shares': shares}

    return render(request, 'sharedfiles.html', d)

def share_file(request, id):
    user = Users.objects.get(id=request.user.id)
    file = Files.objects.get(id=id, owner=user)
    users = Users.objects.exclude(id=user.id)

    if request.method == 'POST':
        user_id = request.POST['user']
        permission = request.POST['permission']
        shared_user = Users.objects.get(id=user_id)

        FileShare.objects.create(file=file, shared_with=shared_user, permission=permission)
        return redirect('/shared_files')
    
    else:
        d = {'file': file, 'users': users}
        return render(request, 'sharefile.html', d)

def remove_share(request, id):
    user = Users.objects.get(id=request.user.id)
    share = FileShare.objects.get(id=id, file__owner=user)
    share.delete()

    return redirect('/shared_files')