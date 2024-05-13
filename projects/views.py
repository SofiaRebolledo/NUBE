from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
import psycopg2
from . import models
from projects.models import Usuario_Registrado
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
import pandas as pd
from projects.models import Usuario_Registrado,INTERNET_MOVIL_CARGO_FIJO_INGRE, INTERNET_MOVIL_DEMANDA_ABONADOS, INTERNET_MOVIL_DEMANDA_TRAFICO, INTERNET_MOVIL_CARGO_FIJO_TRAFI,INTERNET_MOVIL_CARGO_FIJO_SUSCR,INTERNET_MOVIL_DEMANDA_INGRESOS
from projects import Procesamiento



def inicio(request): # OK-----------------------
    return render(request, 'Plantilla.html')

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_superuser == 1:
                login(request,user)
                print("Logueado como admin")
                return redirect("/roladmin/")
            elif user.is_staff == 1:
                login(request,user)
                print("Logueado como analista")
                return redirect("/analista/")
            else:
                login(request,user)
                print("Logueado como usuario")
                return redirect("/inicio/")
        else:
            print("Credenciales incorrectas")
            return redirect("/usuarionoexiste/")
    print("x")
    return render(request,'login.html')


def registro(request): # OK -------------------------------------
    if request.method=='POST':
        nombre =  str((request.POST.get('nombre'))).strip(' ')
        apellido = str(request.POST.get('apellido')).strip(' ')
        telefono= int(request.POST.get('telefono'))
        cedula= int(request.POST.get('cedula'))
        email= str(request.POST.get('email')).strip(' ')
        password= str(request.POST.get('password'))
        username = cedula
        print(username,nombre,apellido,telefono,cedula,email,password)

        #Registrar usuario

        if User.objects.filter(username=username).exists():
            return redirect("/Error/")  
        elif User.objects.filter(email=email).exists():
            return redirect("/Error/")
        else:
            #Registramos el usuario
            user=User()
            user.is_active = 1
            user.username = username
            user.set_password(password)
            user.first_name = nombre
            user.last_name = apellido
            user.email=email
            user.save()
            user2 = models.Usuario_Registrado()
            user2.cedula = cedula
            user2.usuario_id= user.id
            user2.idrol=1
            user2.rol="Usuario"
            user2.save()
            return redirect("/login/")
    return render(request,'registro.html')
    

def forgot_password(request): # FUTURAS VERSIONES --------------------------
    return render(request,'forgot_password.html')

@login_required(login_url="login")
def inicio_admin(request): # OK --------------------------------------------
    return render(request,'inicio_admin.html') 

@login_required(login_url="login")
def historico(request):


    return render(request,'historico.html')

@login_required(login_url="login")
def tendencia(request):
    return render(request,'tendencia.html')

@login_required(login_url="login")
def resultadosindices(request):
    return render(request,'resultadosindices.html')

@login_required(login_url="login")
def roladmin(request): # OK ---------------------
    return render(request,'admin.html') 

@login_required(login_url="login")
def analista(request): # OK ------------------------
    return render(request,'analista.html') 

@login_required(login_url="login")
def crearusuario_admin(request): # OK --------------------
    
    if request.method == 'POST':
        
        rol_seleccionado = request.POST.get('rol')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = cedula
        print(rol_seleccionado)
        print(nombre,apellidos,telefono,cedula,email,password)

        if User.objects.filter(username=username).exists():
            return redirect("/Error/")
        elif User.objects.filter(email=email).exists():
            return redirect("/Error/")
        else:
            #Registramos el usuario
            if rol_seleccionado == "usuario":
                user=User()
                user.is_active = 1
                user.username = username
                user.set_password(password)
                user.first_name = nombre
                user.last_name = apellidos
                user.email = email
                user.is_staff = 0
                user.is_superuser = 0
                user.save()
                user2 = models.Usuario_Registrado()
                user2.cedula = cedula
                user2.usuario_id = user.id
                user2.idrol = 1 
                user2.rol="Usuario"
                user2.save()
            elif rol_seleccionado == "administrador":
                user=User()
                user.is_active = 1
                user.username = username
                user.set_password(password)
                user.first_name = nombre
                user.last_name = apellidos
                user.email = email
                user.is_staff = 0
                user.is_superuser = 1
                user.save()
                user2 = models.Usuario_Registrado()
                user2.cedula = cedula
                user2.usuario_id = user.id
                user2.idrol = 2
                user2.rol="Administrador"
                user2.save()
            else:
                user=User()
                user.is_active = 1
                user.username = username
                user.set_password(password)
                user.first_name = nombre
                user.last_name = apellidos
                user.email = email
                user.is_staff = 1
                user.is_superuser = 0
                user.save()
                user2 = models.Usuario_Registrado()
                user2.cedula = cedula
                user2.usuario_id = user.id
                user2.idrol = 3
                user2.rol="Analista"
                user2.save()
            return redirect("/roladmin/")

    return render(request,'crearusuario_admin.html')

@login_required(login_url="login")
def basedatos_admin(request): # FUTURAS VERSIONES ----------------------
    return render(request,'basedatos_admin.html')

@login_required(login_url="login")
def cargararchivos_analista(request): # OK ------------------------
    if request.method == 'POST':
        uploaded_file = request.FILES['archivo']
        print(uploaded_file)
        if uploaded_file.name.endswith('.xlsx'):
            print("Se sube")
            Procesamiento.handle_uploaded_file(uploaded_file)
            return redirect('/cargararchivos_analista/')
        else:
            return redirect('/Error/')
    return render(request,'cargararchivos_analista.html')

@login_required(login_url="login")
def preprocesamientodatos_analista(request): # FUTURAS VERSIONES -------------
    return render(request,'preprocesamientodatos_analista.html')

@login_required(login_url="login")
def historicodatos_analista(request): # NO SABEMOS QUE SE HARA
    return render(request,'historicodatos_analista.html')

def Error(request): # OK ----------------------
    return render(request,'Error.html')

def usuarionoexiste(request): # OK -------------------------
    return render(request,'usuarionoexiste.html')

def logout(request): #OK ---------------
    # Cerrar sesión del usuario
    django_logout(request)
    # Redirigir a la página de inicio
    return redirect('/inicio/')
