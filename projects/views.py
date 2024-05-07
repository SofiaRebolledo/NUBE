from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import psycopg2

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
        try:
            nombre =  str((request.POST.get('nombre'))).strip(' ')
            apellido = str(request.POST.get('apellido')).strip(' ')
            telefono= int(request.POST.get('telefono'))
            cedula= int(request.POST.get('cedula'))
            email= str(request.POST.get('email')).strip(' ')
            password= str(request.POST.get('password'))
            username = nombre + "_" + apellido + "_" + str(cedula).strip(" ")
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            query = "update public.auth_user set idrol = "+ str(rol) +" where email = '"+ email + "'"
            print(query)
            cur.execute("update public.auth_user set idrol = "+ str(rol) +" where username = '"+ username + "'")
            cur.execute("select * from public.auth_user")
            filas = cur.fetchall()
            for fila in filas:
                print(fila)
            conn.commit()
        except:
            return HttpResponse("Error, usuario ya creado")
        print("Username:  "+username,nombre,apellido,telefono,cedula,email,password)
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
    if request.method == 'GET':
        rol_seleccionado = request.POST.get('rol')
        print(rol_seleccionado)
    if request.method == 'FORM':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(nombre,apellidos,telefono,cedula,email,password)

    return render(request,'crearusuario_admin.html')

def basedatos_admin(request):
    return render(request,'basedatos_admin.html')

def cargararchivos_analista(request):
    return render(request,'cargararchivos_analista.html')

def preprocesamientodatos_analista(request):
    return render(request,'preprocesamientodatos_analista.html')

def historicodatos_analista(request):
    return render(request,'historicodatos_analista.html')
