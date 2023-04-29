from django.urls import path,include

from django.contrib.auth import views

from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('services/', views.Services, name="services"),
    path('service/<int:pk>/', views.Service, name="service"),
    path('work/<int:pk>/', views.Work, name="work"),
    path('works/', views.Works, name="works"),
    path('about/', views.About, name="about"),
    path('blogs/', views.Blogs, name="blogs"),
    path('blog/<int:pk>/', views.Blog, name="blog"),
    path('contact/', views.Contact, name="contact"),

]