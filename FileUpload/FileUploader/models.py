from django.db import models
from django.utils import timezone
import uuid
import os
from django.core.exceptions import ValidationError
# Create your models here.

def FileValidator(file):
    ext = os.path.splitext(file.name)[1]

    if ext.lower() != '.csv':
        raise ValidationError("Import only CSV files")


class FileUploader(models.Model):
    class Meta:
        verbose_name_plural = 'FileUploaders'

    #Naming the fields in the model
    upload_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    file_name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='FileUploader', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', validators=[FileValidator], help_text='Please enter CSV files only')
    upload_date = models.DateTimeField(default=timezone.now)
    upload_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file_name