from django.urls import path
from . import views as v


urlpatterns = [

    path('folders', v.folders),

    path('create_folder', v.create_folder),

    path('rename_folder/<int:id>', v.rename_folder),

    path('delete_folder/<int:id>', v.delete_folder),

    path('open_folder/<int:id>', v.open_folder),

    path('create_subfolder/<int:id>', v.create_subfolder),

    path('move_file/<int:id>', v.move_file),

    path('move_folder/<int:id>', v.move_folder),

]