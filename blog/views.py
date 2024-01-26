from django.shortcuts import render

# Create your views here.


def my_view_blog(request):
    return render(request,'blog/index.html')

def my_view_exemplo(request):
    return render(request,'blog/exemplo.html')
