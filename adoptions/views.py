from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet

def home(request):
    pets=Pet.objects.all()
    # return HttpResponse("<h2>Home View</h2>")
    return render(request,'home.html',{'pets':pets})

def pet_detail(request,id):
    # return HttpResponse("<h2>Home View</h2>")
    try:
        pet=Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet Not Found')
    return render(request,'pet_detail.html',{'pet':pet})

