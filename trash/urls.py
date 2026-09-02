from django.urls import path
from . import views as v

urlpatterns = [
    path('trash', v.trash),
    path('trash_delete/<int:id>', v.delete_file),
    path('trash_restore/<int:id>', v.restore_file),
    path('trash_permanent_delete/<int:id>', v.permanent_delete),
]