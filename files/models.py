from django.db import models
from account.models import Users
from folders.models import Folders
from django import forms

# Create your models here.
class Files(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file = models.FileField()
    description = models.TextField(blank=True)
    folder = models.ForeignKey(Folders, on_delete=models.CASCADE, null=True, blank=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    class Meta:
        db_table = 'files'

class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['file_name', 'file', 'description', 'folder']

class EditFileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['file_name', 'description']