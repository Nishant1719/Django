from django.shortcuts import render
from .models import chaiVarity

# Create your views here.

def all_DjangoApp(request):
    chais = chaiVarity.objects.all()
    return render(request,'DjangoApp/all_DjangoApp.html',{'chais':chais})


def about_app(request):
    return render(request,'DjangoApp/about_app.html')

