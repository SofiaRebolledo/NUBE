from django.shortcuts import render
from django.http.response import JsonResponse
from projects.models import Usuario_Registrado, INTERNET_MOVIL_CARGO_FIJO_INGRE, INTERNET_MOVIL_DEMANDA_ABONADOS, INTERNET_MOVIL_DEMANDA_TRAFICO, INTERNET_MOVIL_CARGO_FIJO_TRAFI, INTERNET_MOVIL_CARGO_FIJO_SUSCR, INTERNET_MOVIL_DEMANDA_INGRESOS
# Create your views here.


def index(request):
    return render(request, 'index.html')


def getchartindices(_request, *args):
    return 0


def getcharttendencia(_request, *args):
    return 0


def getcharthistorico(_request, *args):

    datos = INTERNET_MOVIL_CARGO_FIJO_INGRE.objects.all()
    # Crea listas para almacenar los datos de las columnas que necesitas para el gráfico
    anno_list = []
    empresa_list = []
    ingresos_list = []

    # Itera sobre los datos y agrega las columnas necesarias a las listas
    for dato in datos:
        anno_list.append(dato.ANNO)
        empresa_list.append(dato.EMPRESA)
        ingresos_list.append(dato.INGRESOS)

    datos_combinados = list(zip(anno_list, empresa_list, ingresos_list))
    datos_combinados.sort(key=lambda x: x[0])

    solo_anos = [tupla[0] for tupla in datos_combinados]
    solo_empresas = [tupla[1] for tupla in datos_combinados]
    solo_ingresos = [tupla[2] for tupla in datos_combinados]

    chart = {
        'tooltip': [
            {
                'trigger': 'axis'
            }
        ],
        'xAxis': [
            {
                'type': "category",
                'data': solo_anos
            }
        ],
        'yAxis': [
            {
                'type': "value"
            }
        ],
        'series': []
    }

    for empresa in set(solo_empresas):
        series_data = [ingresos for anno, emp, ingresos in zip(
            solo_anos, solo_empresas, solo_ingresos) if emp == empresa]
        series = {
            'name': empresa,
            'type': 'line',
            'data': series_data
        }

        chart['series'].append(series)
    return JsonResponse(chart)
