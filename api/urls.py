from django.urls import path
from api import views

urlpatterns = [
    path('',views.index,name='index'),
    path('get_chart_historico/',views.getcharthistorico,name='getcharthistorico'),
    path('get_chart_indices/',views.getchartindices,name='getchartindices'),
    path('get_chart_tendencia/',views.getcharttendencia,name='getcharttendencia')
]
