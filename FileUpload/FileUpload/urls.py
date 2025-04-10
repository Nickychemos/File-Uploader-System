"""
URL configuration for FileUpload project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from FileUploader.views import GetFileUploadAPIViews, DelFileUploadAPIViews, AddFileUploaderAPIViews, DetailsFileUploadAPIView
from FileUploader.views import UserListViews, UserDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('rest_framework.urls')),
    path('get-upload/', GetFileUploadAPIViews.as_view(), name='GetFileUploadAPIViews'),
    path('delete-upload/', DelFileUploadAPIViews.as_view(), name='DelFileUploadAPIViews'),
    path('post-upload/', AddFileUploaderAPIViews.as_view(), name='AddFileUploaderAPIViews'),
    path('upload-details/', DetailsFileUploadAPIView.as_view(), name='DetailsFileUploadAPIView'),
    path('upload-users/', UserListViews.as_view(), name = 'Users'),
    path('upload-details/', UserDetails.as_view(), name = 'UserDetails')
]
