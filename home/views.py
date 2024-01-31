from django.shortcuts import render

# Create your views here.
def my_view_home(request):
    contexto = {
        'text': 'texto como context parametro....... HOME',
        'title': 'Pagina Inicial - ',

        }
    return render(request,'home/index.html', contexto)
