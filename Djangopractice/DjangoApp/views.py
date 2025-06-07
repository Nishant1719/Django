from django.shortcuts import render
from .models import chaiVarity
from django.shortcuts import get_object_or_404
# Create your views here.

def all_DjangoApp(request):
    chais = chaiVarity.objects.all()
    return render(request,'DjangoApp/all_DjangoApp.html',{'chais':chais})


def about_app(request):
    return render(request,'DjangoApp/about_app.html')

def give_description(request,id):
    chai = get_object_or_404(chaiVarity, pk=id)
    return render(request,'DjangoApp/chai_description.html',{'chai':chai})
    