# Generated by Django 2.2.1 on 2019-08-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_blogcategory_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='category_image',
            field=models.ImageField(default='category/default.jpg', upload_to='category/'),
        ),
    ]
