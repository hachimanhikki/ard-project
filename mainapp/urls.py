from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('servicePage/<str:serviceName>/', views.service, name='service'),
    path('search/', views.search, name='search')
]
