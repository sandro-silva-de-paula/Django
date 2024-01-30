from django.shortcuts import render

# Create your views here.
def my_view_home(request):
    contexto = {
        'text': 'texto como context parametro.......',
        'text_2': 'ola home',
         'title': 'Home - ',
         'text_part': 'testando partial head -  vindo do home',
         'text_parag': 'paragrafo..............'
        }
    return render(request,'home/index.html', contexto)
