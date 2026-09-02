from django.urls import path
from . import views as v

urlpatterns = [

    path('filenest', v.filenest),

    path('upload_file', v.upload_file),

    path('edit_file/<int:id>', v.edit_file),

    path('file_details/<int:id>', v.file_details),

    path('download_file/<int:id>', v.download_file),

    path('delete_file/<int:id>', v.delete_file),

    path('preview_file/<int:id>', v.preview_file),
    path('files', v.show_files),
]