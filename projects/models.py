import email
import uuid
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models

# Create your models here.
    
class Usuario(models.Model):
    documento = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    nombre = models.CharField(max_length=200)
    email = models.TextField(null=True,blank=True)

class Analista(models.Model):
    document = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True,editable=False)
    nombre = models.CharField(max_length=200)
    email = models.TextField(null=True,blank=True)

def _str_(self):
    return self.name