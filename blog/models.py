from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    # if no default is defined, add attribute null=True, blank=True
    cover_image = models.ImageField(upload_to="blogs", default="static/default_blog.jpg")
    # Execute makemigrations to create migration file and migrate to populate in database

    def trunc_body(self):
        trunc_body = self.body[:100]
        if len(trunc_body) >= 100:
            return "{0} ...".format(
                self.body[:100]
            )
        else:
            return trunc_body

    def __str__(self):
        return self.title