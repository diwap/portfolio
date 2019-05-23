from django.urls import path

from about.views import aboutme

urlpatterns = [
    path('', aboutme, name="about_me"),
]