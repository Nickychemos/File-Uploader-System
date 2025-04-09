from django.contrib import admin
from .models import FileUploader

# Register your models here.
@admin.register(FileUploader)

class FileUploaderAdmin(admin.ModelAdmin):
    list_display = ['upload_id', 'file_name',
                     'file', 'upload_date', 'upload_description']
    search_fields = ['upload_id', 'file_name',
                      'file', 'upload_date', 'upload_description']