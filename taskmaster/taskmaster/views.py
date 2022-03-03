from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Эта страница')

def home(request):
    return render(request, 'home.html', {'greeting': 'Hello my sweet home !!! '})