from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def contact_me(request):
    if request.method == 'POST':
        def req(value):
            return request.POST.get(value, None)

        send_mail(
            'You have received a new email from {0} - {1}'.format(
                req('contact_name'),
                req('email')
            ),
            req('body'),
            settings.EMAIL_HOST_USER,
            ['dipipandey1@gmail.com'],
            fail_silently=False
        )
        
        
    return render(request, 'contact/contact.html')