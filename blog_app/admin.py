from django.contrib import admin
from blog_app.models import *
# Register your models here.

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','created')
admin.site.register(BlogCategory,BlogCategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    def category(self,obj):
        return obj.category_name
    list_display = ('category','title')
admin.site.register(Blog,BlogAdmin)