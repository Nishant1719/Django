from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello, World! Home page")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, World! about page")

def contact(request):
    return HttpResponse("Hello, World! contact page")



