from django.shortcuts import render
from blog.data import posts

# Create your views here.


def my_view_blog(request):
    contexto = {
        'text': 'texto como context parametro....... index blog',
        'title': 'Blog Inicial - ',
        'posts': posts
        }
    return render(request,'blog/index.html', contexto)

def my_view_exemplo(request):
    contexto = {
        'text': 'texto como context parametro.......exemplo',
        'title': 'Exemplo Inicial - ',
        'posts': posts
             }
    return render(request,'blog/exemplo.html', contexto)
