from rcb.views import *
from django.urls import path


urlpatterns=[
    path('royal/',royal,name='royal'),
    path('max/',max,name='max'),
    path('maxwel/',maxwel,name='maxwel'),
    path('rayudu/',rayudu,name='rayudu'),

]