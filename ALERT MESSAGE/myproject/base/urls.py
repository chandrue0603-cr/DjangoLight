from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('success/',success,name='Success'),
    path('info/',info,name='Info'),
    path('error/',error,name='Danger'),
    path('warning/',warning,name='Warning'),
    
]