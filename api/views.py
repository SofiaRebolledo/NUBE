from django.shortcuts import render
from django.http.response import JsonResponse
from random import randrange
# Create your views here.


def index(request):
    return render(request, 'index.html')


def getchart(_request):

    serie = []
    counter = 0

    while (counter < 7):
        serie.append(randrange(100, 400))
        counter = counter + 1

    chart = { 
        'xAxis': [
            {
                'type':"category",
                'data': ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            }
        ],
        'yAxis':[
            {
                'type': "value"
            }
        ],
        'series':[
            {
                'data':serie,
                'type': "line"
            }
        ]
    }

    return JsonResponse(chart)
