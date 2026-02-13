from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')
def success(request):
    messages.success(request,'This is Success Message')
    return render(request, 'home.html')
def info(request):
    messages.info(request,'This is Info Message')
    return render(request, 'home.html')
def error(request):
    messages.error(request,'This is Error Message')
    return render(request, 'home.html')
def warning(request):
    messages.warning(request,'This is Warning Message')
    return render(request, 'home.html')
