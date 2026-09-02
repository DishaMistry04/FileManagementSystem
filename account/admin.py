from django.contrib import admin
from . models import Users

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','contact']

admin.site.register(Users,UserAdmin)