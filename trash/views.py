from django.shortcuts import render, redirect
from .models import Trash
from files.models import Files
from account.models import Users

def trash(request):
    user = Users.objects.get(id=request.user.id)
    trash_files = Trash.objects.filter(deleted_by=user)
    d = {'trash_files': trash_files}

    return render(request, 'trash.html', d)

def delete_file(request, id):
    user = Users.objects.get(id=request.user.id)
    file = Files.objects.get(id=id, owner=user)
    Trash.objects.create(file=file, deleted_by=user)

    return redirect('/files')

def restore_file(request, id):
    user = Users.objects.get(id=request.user.id)
    trash = Trash.objects.get(id=id, deleted_by=user)
    trash.delete()

    return redirect('/trash')

def permanent_delete(request, id):
    user = Users.objects.get(id=request.user.id)
    trash = Trash.objects.get(id=id, deleted_by=user)
    file = trash.file
    file.file.delete()
    file.delete()

    return redirect('/trash')