from django.shortcuts import render,HttpResponse


# views.py
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

#
from twilio.rest import Client
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,"home.html")