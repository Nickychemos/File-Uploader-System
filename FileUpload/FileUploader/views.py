from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser

from .models import FileUploader
from .serializer import FileUploadSerializer

# Create your views here.

#Object to obtain all files
class GetFileUploadAPIViews(APIView):

    #Defining a method to get all uploaded files 
    def get(self, request, *args, **kwargs):
        files = FileUploader.objects.all()
        serializer = FileUploadSerializer(files, data = request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Object to delete files
class DelFileUploadAPIViews(APIView):

    #Defining a delete function
    def delete(self, request, upload_id):
        try:
            files = FileUploader.objects.get(upload_id = upload_id)
        except files.DoesNotExist:
            return Response({"Error": "Your file does not exist"}, status=status.HTTP_404_NOT_FOUND)
        files.delete()
        return Response("File deleted successfully", status=status.HTTP_204_NO_CONTENT)
    
#Object to upload files

class AddFileUploaderAPIViews(APIView):

    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    #Defining a method to add file uploads
    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Object to obtain details of specific files

class DetailsFileUploadAPIView(APIView):

    #Defining a function to get the details
    def details(self, request, upload_id):
        try:
            files = FileUploader.objects.get(upload_id = upload_id)
        except files.DoesNotExist:
            return Response({"Error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FileUploadSerializer(files, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)