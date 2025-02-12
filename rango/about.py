from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse(
        "Rango says here is the about page. <br><a href='/rango/'>Go to Home Page</a>"
    )