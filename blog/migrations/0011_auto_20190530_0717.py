# Generated by Django 2.2.1 on 2019-05-30 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_blog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='blog',
            name='total_views',
            field=models.IntegerField(default=1),
        ),
    ]
