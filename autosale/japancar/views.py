from django.shortcuts import redirect, render

from .models import Auto_new

# Create your views here.

def index(request):
    return render(request,'showroom/index.html')

def about(request):
    return render(request,'showroom/about.html')

def list_of_cars(request):

    context = {'cars': Auto_new.objects.all()}
    return render(request,'showroom/list_of_cars.html',context=context)
