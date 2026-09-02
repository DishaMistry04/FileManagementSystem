from django.urls import path
from . import views as v

urlpatterns = [
    path('shared_files', v.shared_files),
    path('share_file/<int:id>', v.share_file),
    path('remove_share/<int:id>', v.remove_share),
]