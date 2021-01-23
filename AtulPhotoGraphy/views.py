from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.models import *


def showPage(request):
    images = Image.objects.all()
    categories = Category.objects.all()

    data = {'images':images,'categories':categories}
    
    return render(request, 'index.html',data)


def showCatPage(request,cid):
    images = Image.objects.all()
    cats = Category.objects.all()
    print(cid)
    category = Category.objects.get(pk=cid)
    
    images = Image.objects.filter(cat=category)
    data = {'images':images,'categories':cats}
    
    return render(request, 'index.html',data)