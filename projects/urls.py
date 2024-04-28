from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio , name="inicio"),
    path('login/', views.login, name="login"),
    path('registro/', views.registro, name="registro"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('inicio_admin/', views.inicio_admin, name="inicio_admin"),
    path('calendario/', views.inicio_admin, name="calendario"),
    #cambiossss
]
