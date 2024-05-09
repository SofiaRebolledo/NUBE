from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import psycopg2
from . import models
from projects.models import Usuario_Registrado


conn = psycopg2.connect(
    dbname="projects",
    user="postgres",
    password="admin",
    host="localhost",
    port ="5432"
)
cur = conn.cursor()

def inicio(request):
    return render(request, 'Plantilla.html')

def login(request):
    return render(request,'login.html')

def registro(request):
    rol = 3
    if request.method=='POST':
        nombre =  str((request.POST.get('nombre'))).strip(' ')
        apellido = str(request.POST.get('apellido')).strip(' ')
        telefono= int(request.POST.get('telefono'))
        cedula= int(request.POST.get('cedula'))
        email= str(request.POST.get('email')).strip(' ')
        password= str(request.POST.get('password'))
        username = nombre + "_" + apellido + "_" + str(cedula).strip(" ")
        cur.execute("select * from public.auth_user")
        filas = cur.fetchall()
        for fila in filas:
            print(fila)
        print("Username:  "+username,nombre,apellido,telefono,cedula,email,password)

        #Registrar usuario
        if User.objects.filter(username=username).exists():
            return HttpResponse("Ya existe el usuario")
        elif User.objects.filter(email=email).exists():
            return HttpResponse("El correo ya existe")
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
            return HttpResponse("Registro completado")
    return render(request,'registro.html')
    

def forgot_password(request):
    return render(request,'forgot_password.html')

def inicio_admin(request):
    return render(request,'inicio_admin.html')

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
    
    if request.method == 'POST':
        
        rol_seleccionado = request.POST.get('rol')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = nombre + "_" + apellidos + "_" + str(cedula).strip(" ")
        print(rol_seleccionado)
        print(nombre,apellidos,telefono,cedula,email,password)

        if User.objects.filter(username=username).exists():
            return HttpResponse("Ya existe el usuario")
        elif User.objects.filter(email=email).exists():
            return HttpResponse("El correo ya existe")
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
            return HttpResponse("Registro completado")

    return render(request,'crearusuario_admin.html')

def basedatos_admin(request):
    return render(request,'basedatos_admin.html')

def cargararchivos_analista(request):
    return render(request,'cargararchivos_analista.html')

def preprocesamientodatos_analista(request):
    return render(request,'preprocesamientodatos_analista.html')

def historicodatos_analista(request):
    return render(request,'historicodatos_analista.html')
