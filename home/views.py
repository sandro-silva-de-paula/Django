from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_view_home(request):
    return HttpResponse('Uma mensagem para alguem especial em Home em home app_1')