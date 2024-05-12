import email
import uuid
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario_Registrado(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    cedula = models.IntegerField()
    idrol = models.IntegerField(default=1)
    rol = models.TextField(max_length=100,default="Usuario")

    def __str__(self):
        return "%s the user_registered" % self.cedula

class INTERNET_MOVIL_CARGO_FIJO_INGRE(models.Model):
    id = models.AutoField(primary_key=True)
    ANNO = models.IntegerField()
    TRIMESTRE = models.IntegerField()
    MES_DEL_TRIMESTRE = models.IntegerField()
    ID_EMPRESA = models.IntegerField()
    EMPRESA = models.CharField(max_length=100)
    ID_SEGMENTO	= models.IntegerField()
    SEGMENTO = models.TextField(max_length=100,default="Personas")
    ID_TERMINAL	= models.IntegerField()
    TERMINAL = models.TextField(max_length=100,default="Teléfono móvil")
    INGRESOS = models.BigIntegerField()


    def __str__(self):
        return f'{self.EMPRESA} - Trimestre {self.TRIMESTRE} del año {self.ANNO}'  

class INTERNET_MOVIL_DEMANDA_ABONADOS(models.Model):
    #id = models.AutoField(primary_key=True)
    ANNO = models.IntegerField()
    TRIMESTRE = models.IntegerField()
    MES_DEL_TRIMESTRE = models.IntegerField()
    ID_EMPRESA = models.IntegerField()
    EMPRESA = models.CharField(max_length=100)
    ID_MODALIDAD_PAGO = models.TextField()
    MODALIDAD_PAGO = models.CharField(max_length=100)
    ID_TERMINAL = models.IntegerField()
    TERMINAL = models.CharField(max_length=100)
    ID_TECNOLOGIA = models.IntegerField()
    TECNOLOGIA = models.CharField(max_length=100)
    CANTIDAD_ABONADOS = models.IntegerField()

    def __str__(self):
        return f'{self.EMPRESA} - Trimestre {self.TRIMESTRE} del año {self.ANNO}'
    
class INTERNET_MOVIL_DEMANDA_TRAFICO(models.Model):
    #id = models.AutoField(primary_key=True)
    ANNO = models.IntegerField()
    TRIMESTRE = models.IntegerField()
    MES_DEL_TRIMESTRE = models.IntegerField()
    ID_EMPRESA = models.IntegerField()
    EMPRESA = models.CharField(max_length=100)
    ID_MODALIDAD_PAGO = models.TextField()
    TRAFICO = models.BigIntegerField()
    MODALIDAD_PAGO = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.EMPRESA} - Trimestre {self.TRIMESTRE} del año {self.ANNO}'

class INTERNET_MOVIL_CARGO_FIJO_TRAFI(models.Model):
    #id = models.AutoField(primary_key=True)
    ANNO = models.IntegerField()
    TRIMESTRE = models.IntegerField()
    MES_DEL_TRIMESTRE = models.IntegerField()
    ID_EMPRESA = models.IntegerField()
    EMPRESA = models.CharField(max_length=100)
    TRAFICO = models.BigIntegerField()

    def __str__(self):
        return f'{self.EMPRESA} - Trimestre {self.TRIMESTRE} del año {self.ANNO}'


class INTERNET_MOVIL_CARGO_FIJO_SUSCR(models.Model):
    #id = models.AutoField(primary_key=True, verbose_name="ID")
    ANNO = models.IntegerField()
    TRIMESTRE = models.IntegerField()
    MES_DEL_TRIMESTRE = models.IntegerField()
    ID_SEGMENTO = models.IntegerField()
    SEGMENTO = models.TextField()
    ID_EMPRESA = models.IntegerField()
    EMPRESA = models.TextField()
    ID_TERMINAL = models.IntegerField()
    TERMINAL = models.TextField()
    ID_TECNOLOGIA = models.IntegerField()
    TECNOLOGIA = models.TextField()
    CANTIDAD_SUSCRIPTORES = models.IntegerField()

    def __str__(self):
        return f'{self.EMPRESA} - Trimestre {self.TRIMESTRE} del año {self.ANNO}'


class INTERNET_MOVIL_DEMANDA_INGRESOS(models.Model):
    #id = models.AutoField(primary_key=True)
    ANNO = models.IntegerField()
    TRIMESTRE = models.IntegerField()
    MES_DEL_TRIMESTRE = models.IntegerField()
    ID_EMPRESA = models.IntegerField()
    EMPRESA = models.CharField(max_length=100)
    ID_MODALIDAD_PAGO = models.TextField()
    MODALIDAD_PAGO = models.CharField(max_length=100)
    ID_TERMINAL = models.IntegerField()
    TERMINAL = models.TextField()
    INGRESOS = models.BigIntegerField()

    def __str__(self):
        return f'{self.EMPRESA} - Trimestre {self.TRIMESTRE} del año {self.ANNO}'
