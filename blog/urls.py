
from django.urls import path
from blog import views 


urlpatterns = [
    path('', views.my_view_blog),
    path('exemplo/', views.my_view_exemplo),

]
