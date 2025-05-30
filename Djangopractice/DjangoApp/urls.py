from django.contrib import admin
from django.urls import path
from . import views

#localhost:8000/DjangoApp
#localhost:8000/DjangoApp/about/
urlpatterns = [
    path('',views.all_DjangoApp,name="all_DjangoApp"),
    path('/about/',views.about_app,name="about_app"),
]
