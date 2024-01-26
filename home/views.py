from django.shortcuts import render

# Create your views here.
def my_view_home(request):
    return render(request,'home/index.html')
