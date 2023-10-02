from django.contrib import admin

# Register your models here.
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display=['title','category','description','date']

admin.site.register(Todo,TodoAdmin)