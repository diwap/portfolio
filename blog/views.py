from django.shortcuts import render

from blog.models import Blog, Comment


# def view_counter(id):
#     ptv = Blog.objects.get(pk=id)
#     ptv.total_views = ptv.total_views + 1
#     ptv.save()

def blog_list(request):
    context = {
        'blog': Blog.objects.all()
    }
    return render(request, 'blog/index.html', context)

def blog_detail(request, id):

    if request.method == 'GET':
        ptv = Blog.objects.get(pk=id)
        ptv.total_views = ptv.total_views + 1
        ptv.save()

    if request.method == 'POST':
        created_by = request.POST.get('created_by', None)
        body = request.POST.get('body', None)

        if created_by and body:
            blog = Blog.objects.get(pk=id)
            comnt = Comment(created_by=created_by, body=body, blog=blog)
            comnt.save()
    
    context = {
        'blog': Blog.objects.get(pk=id),
        'comment': Comment.objects.filter(blog=id)
    }
    return render(request, 'blog/blog_detail.html', context)