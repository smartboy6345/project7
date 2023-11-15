from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('<marquee><h1> SURESH RAINA   MR.IPL NO ONE ALL ROUNDER IN CSK</h1></marquee>')