from .models import FileUploader
from rest_framework import serializers
from django.contrib.auth.models import User

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploader
        fields = ['upload_id', 'file_name', 'file',
                   'upload_date', 'upload_description']

class UserSerializer(serializers.ModelSerializer):
    files = serializers.PrimaryKeyRelatedField(many = True, queryset = FileUploader.objects.all(), source = 'FileUploader')
    # serializer = serializers.ReadOnlyField(source = 'owner.username')

    class Meta:
        model = User
        fields = ['id', 'files', 'username']