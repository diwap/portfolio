from django.shortcuts import render, HttpResponse


def contact_me(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'contact/contact.html')