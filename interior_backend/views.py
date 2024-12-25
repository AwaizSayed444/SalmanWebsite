from django.shortcuts import render,HttpResponse

# Create your views here.

def home_view():
    return HttpResponse("This is my repsonse")