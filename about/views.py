from django.shortcuts import HttpResponse


def aboutme(request):
    return HttpResponse("About Me, Hello")