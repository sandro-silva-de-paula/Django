
from django.urls import path
from home import views 


urlpatterns = [
    path('', views.my_view_home),

]
