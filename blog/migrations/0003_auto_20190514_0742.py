# Generated by Django 2.2.1 on 2019-05-14 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_image',
            field=models.ImageField(default='static/default_blog.jpg', upload_to='blogs'),
        ),
    ]
