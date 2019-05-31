from django.urls import path

from blog.views import blog_list, blog_detail, search_blogs


urlpatterns = [
    path('', blog_list, name="blog_list"),
    path('<int:id>', blog_detail, name="blog_detail"),
    path('search', search_blogs, name="search_blogs")
]