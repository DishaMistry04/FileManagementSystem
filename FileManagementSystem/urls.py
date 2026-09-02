from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('',include('ai.urls')),
    path('',include('files.urls')),
    path('',include('folders.urls')),
    path('',include('filesharing.urls')),
    path('',include('trash.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
