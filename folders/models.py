from django.db import models
from account.models import Users
from django import forms

# Create your models here.
class Folders(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folder_name
    
    class Meta:
        db_table = 'folders'


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folders
        fields = ['folder_name', 'parent']