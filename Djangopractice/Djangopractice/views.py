from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World! Home page")

def about(request):
    return HttpResponse("Hello, World! about page")

def contact(request):
    return HttpResponse("Hello, World! contact page")



