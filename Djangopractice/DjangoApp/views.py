from django.shortcuts import render,redirect
from .models import ChaiVariety
from django.shortcuts import get_object_or_404
# Create your views here.

def all_DjangoApp(request):
    chais = ChaiVariety.objects.all()
    return render(request,'DjangoApp/all_DjangoApp.html',{'chais':chais})


def about_app(request):
    return render(request,'DjangoApp/about_app.html')

# def give_description(request,id):
#     chai = get_object_or_404(chaiVarity, pk=id)
    # if chai == None: # I cannot do this way as it directly raises 404 if object is not found
#         redirect('DjangoApp/')
#     return render(request,'DjangoApp/chai_description.html',{'chai':chai})
# Alternately:
def give_description(request, id):
    try:
        chai = ChaiVariety.objects.get(pk=id) #
    except ChaiVariety.DoesNotExist:
        return redirect('/DjangoApp') 
    return render(request, 'DjangoApp/chai_description.html', {'chai': chai})