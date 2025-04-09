# Generated by Django 5.2 on 2025-04-09 14:26

import FileUploader.models
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('file_name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='uploads/', validators=[FileUploader.models.FileValidator])),
                ('upload_date', models.TimeField(default=django.utils.timezone.now)),
                ('upload_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'FileUploaders',
            },
        ),
    ]
