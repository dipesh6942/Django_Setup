from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render (request,"djangoApp/home.html",context)

def xyz(request):
    return render(request,"djangoApp/xyz.html")