from django.urls import path

from contact.views import contact_me

urlpatterns = [
    path('', contact_me, name="contact_me")
]