# Generated by Django 2.2.1 on 2019-05-24 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blog_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(default='Anonymous', max_length=50)),
            ],
        ),
    ]
