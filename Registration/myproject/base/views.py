from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        address=request.POST['address']
        mail=request.POST['mail']
        return render(request,'register.html',{
            'Name':name,
            'Password':password,
            'Address':address,
            'Mail':mail})
    return render(request, 'register.html')
