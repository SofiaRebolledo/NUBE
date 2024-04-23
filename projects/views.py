from django.shortcuts import render, redirect
from django.http import HttpResponse

def projects(request):
    return render(request, 'Plantilla.html')

def project(request, pk):
    return render(request, 'oooooooooo.html')

def login(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'registro.html')

def forgot_password(request):
    return render(request,'forgot_password.html')

def inicio_admin(request):
    return render(request,'inicio_admin.html')

def calendario(request):
    return render(request,'calendario.html')