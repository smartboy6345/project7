from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def royal(request):
    return render(request,'royal.html')
def max(request):
    return HttpResponse('<marquee><h1>Maxwell is one of the most famous player in the word</h1></marquee>')
def maxwel(request):
    return HttpResponse('<center><h1>Max well breaked history recently by hitting 200+ in 110 balls</h1></center>')
def rayudu(request):
    return render(request,'amabati.html')