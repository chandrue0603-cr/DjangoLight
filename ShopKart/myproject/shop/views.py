from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def collections(request):
    category=Category.objects.filter(status=0)
    return render(request, 'collections.html',{"category":category})