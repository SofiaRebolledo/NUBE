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

