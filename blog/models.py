from django.db import models
from tinymce.models import HTMLField

from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField(default="No content")

    # if no default is defined, add attribute null=True, blank=True
    cover_image = models.ImageField(upload_to="blogs", default="static/default_blog.jpg")
    # Execute makemigrations to create migration file and migrate to populate in database

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    total_views = models.IntegerField(default=1)

    def trunc_body(self):
        trunc_body = self.content[:100]
        if len(trunc_body) >= 100:
            return "{0} ...".format(
                self.content[:100]
            )
        else:
            return trunc_body

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-total_views"]

class Comment(models.Model):
    body = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    created_by = models.CharField(max_length=50, default="Anonymous")

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_date']