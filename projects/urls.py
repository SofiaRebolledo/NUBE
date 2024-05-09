from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio , name="inicio"),
    path('inicio/', views.inicio , name="inicio"),
    path('login/', views.login1, name="login"),
    path('registro/', views.registro, name="registro"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('inicio_admin/', views.inicio_admin, name="inicio_admin"),
    path('historico/', views.historico, name="historico"),
    path('tendencia/', views.tendencia, name="tendencia"),
    path('resultadosindices/', views.resultadosindices, name="resultadosindices"),
    path('roladmin/', views.roladmin, name="roladmin"),
    path('analista/', views.analista, name="analista"),
    path('crearusuario_admin/', views.crearusuario_admin, name="crearusuario_admin"),
    path('basedatos_admin/', views.basedatos_admin, name="basedatos_admin"),
    path('cargararchivos_analista/', views.cargararchivos_analista, name="cargararchivos_analista"),
    path('preprocesamientodatos_analista/', views.preprocesamientodatos_analista, name="preprocesamientodatos_analista"),
    path('historicodatos_analista/', views.historicodatos_analista, name="historicodatos_analista"),
    path('Error/', views.Error, name="Error"),
    path('usuarionoexiste/', views.usuarionoexiste, name="usuarionoexiste"),
]