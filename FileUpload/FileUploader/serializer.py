from .models import FileUploader
from rest_framework import serializers

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploader
        fields = ['upload_id', 'file_name', 'file',
                   'upload_date', 'upload_description']

