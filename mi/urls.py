from csk.views import *
from mi.views import *
from django.urls import path
app_name='anything'

urlpatterns=[
    path('bombay1/',bombay1,name='bombay1'),
    path('mumbai/',mumbai,name='mumbai'),
]