from django.urls import path
from . import views as v

urlpatterns = [
    path('summary/<int:id>', v.file_summary)
]
