from django.contrib.auth.models import User
from rest_framework import serializers
from blog_app.models import *


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = (
            'id',
            'owner',
            'created',
            'updated'
        )

class BlogCategorySerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many = True, read_only = True)
    class Meta:
        model = BlogCategory
        fields = '__all__'
        read_only_fields = (
            'id',
            'slug',
            'created',
            'updated'
        )


class UserSerializer(serializers.ModelSerializer):
    user_blogs = BlogSerializer(many = True, read_only = True)
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'id','date_joined','last_login','groups','user_permissions',
        )
    def create(self,validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user