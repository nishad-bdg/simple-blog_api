from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.http import Http404
from rest_framework import status
#from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes,renderer_classes
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from blog_app.models import *
from blog_app.serializers import *
# Create your views here.

class CategoryList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BlogCategorySerializer
    
    def get(self,request,format = None):
        instance = BlogCategory.objects.all()
        serializer = BlogCategorySerializer(instance, many = True)
        return Response(serializer.data)

    def post(self,request,format = None):
        response = {}
        serializer = BlogCategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response["success"] = "Category created successfully"
            return Response(response,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class BlogList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BlogSerializer
    
    def get(self,request,format = None):
        instance = Blog.objects.all()
        serializer = BlogSerializer(instance, many = True)
        return Response(serializer.data)

    def post(self,request,format = None):
        response = {}
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['owner'] = request.user
            serializer.save()
            response["success"] = "Blog posted successfully"
            return Response(response,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class BlogDetail(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BlogSerializer

    def get_object(self, pk):
        try:
            return Blog.objects.get(pk = pk)
        except Blog.DoesNotExist:
            raise Http404

    def get(self,request,pk,format = None):
        instance = self.get_object(pk)
        serializer = BlogSerializer(instance)
        return Response(serializer.data)

    def patch(self,request,pk,format = None):
        response = {}
        instance = self.get_object(pk)
        if request.user.is_superuser:
            serializer = BlogSerializer(
                instance, 
                data =  request.data, 
                partial = True
            )
            if serializer.is_valid():
                serializer.save()
                response["success"] = "Blog updated successfully"  
                return Response(response, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"errors":["Access denied"]},status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format = None):
        instance = self.get_object(pk)
        if request.user.is_superuser:
            instance.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            return Response({"errors":["Access denied"]},status = status.HTTP_400_BAD_REQUEST)

class UserBlogList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self,request,format = None):
        instance = User.objects.get(username = request.user)
        serializer = UserSerializer(instance)
        return Response(serializer.data)