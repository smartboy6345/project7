from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bombay1(request):
    return render(request,'bombay.html')

def mumbai(request):
    return HttpResponse('<marquee<h1> top MNC companies are their in mumbai</h1></marquee>')