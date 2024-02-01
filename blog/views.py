from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404 

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

def my_view_post(request:HttpRequest,_id: int):
    found_post : dict[str,Any] | None = None
    for post in posts:
        if post['id'] == _id:
           found_post=post
           break 
    # pra nao ficar dando erro de tipo em found_post    
    if found_post is None:
        raise Http404('Post inesixtente')    

    contexto = {
        'text': 'texto como context parametro.......post',
        'title': found_post['title'] +'- ',
        'post': found_post
                                  }
    return render(request,'blog/post.html', contexto)
