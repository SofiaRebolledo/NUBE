from django.shortcuts import render, redirect
from django.http import HttpResponse

def inicio(request):
    return render(request, 'Plantilla.html')

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

def historico(request):
    return render(request,'historico.html')

def tendencia(request):
    return render(request,'tendencia.html')

def resultadosindices(request):
    return render(request,'resultadosindices.html')

def roladmin(request):
    return render(request,'admin.html')

def analista(request):
    return render(request,'analista.html')

def crearusuario_admin(request):
    return render(request,'crearusuario_admin.html')
