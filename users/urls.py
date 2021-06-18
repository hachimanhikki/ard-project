from django.urls import path, include
from . import views

urlpatterns = [
    path('loginPage/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registerPage/', views.registerPage, name='register'),
    path('profile/', views.profile, name='profile'),
]