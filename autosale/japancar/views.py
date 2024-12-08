from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    return render(request,'showroom/index.html')

def about(request):
    return render(request,'showroom/about.html')
