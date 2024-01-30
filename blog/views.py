from django.shortcuts import render

# Create your views here.


def my_view_blog(request):
    contexto = {
        'text': 'texto como context parametro....... index',
        'text_2': 'ola blog',
        'title': 'BLog inicial - ',
        'text_part': 'testando partial head - vindo  blog',
        'text_parag': 'paragrafo.............. do blog'
        }
    return render(request,'blog/index.html', contexto)

def my_view_exemplo(request):
    contexto = {
        'text': 'texto como context parametro.......exemplo',
        'text_2': 'ola exemplo',
        'title': 'Blog_exemplo - ',
        'text_part': 'testando partial head - vindo do exemplo',
        'text_parag': 'paragrafo.............. Exemplo'
                }
    return render(request,'blog/exemplo.html', contexto)
