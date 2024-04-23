from django.shortcuts import render, redirect
from django.http import HttpResponse

def projects(request):
    return render(request, 'Plantilla.html')

def project(request, pk):
    return render(request, 'oooooooooo.html')

def login(request):
    return render(request,'registro.html')