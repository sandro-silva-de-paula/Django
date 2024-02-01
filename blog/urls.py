
from django.urls import path
from blog import views 

app_name = 'blog'
urlpatterns = [
    path('', views.my_view_blog,name='blog'),
    path('post/<int:_id>', views.my_view_post,name='post'),
    path('exemplo/', views.my_view_exemplo, name='exemplo'),

]
