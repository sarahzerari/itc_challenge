from django.conf import settings
from .import views
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [
     path("",views.home, name="home"),
     path('register/', views.register, name='register'),
     path('succes/', views.succes, name='succes')
    ]