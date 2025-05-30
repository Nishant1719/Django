from django.shortcuts import render

# Create your views here.

def all_DjangoApp(request):
    return render(request,'DjangoApp/all_DjangoApp.html')


def about_app(request):
    return render(request,'DjangoApp/about-app.html')