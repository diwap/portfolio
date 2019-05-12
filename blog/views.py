from django.shortcuts import render

from blog.models import Blog


def blog_list(request):
    context = {
        'blog': Blog.objects.all()
    }
    return render(request, 'blog/index.html', context)
