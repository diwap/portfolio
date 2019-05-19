from django.shortcuts import render

from blog.models import Blog


def blog_list(request):
    context = {
        'blog': Blog.objects.all()
    }
    return render(request, 'blog/index.html', context)

def blog_detail(request, id):
    context = {
        'blog': Blog.objects.get(pk=id)
    }
    return render(request, 'blog/blog_detail.html', context)