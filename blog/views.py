from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def my_view_blog(request):
    return HttpResponse('Uma mensagem para alguem especial em Blog do blog app_1')

def my_view_exemplo(request):
    return HttpResponse('Uma mensagem para alguem especial em Blog do blog  exemplo app_1')