# Generated by Django 2.2.1 on 2019-05-24 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190523_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
    ]