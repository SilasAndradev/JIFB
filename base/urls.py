from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomePage, name='home'),

    path('404', views.NotFoundPage, name='404'),

    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('register/', views.RegisterUser, name='register'),

    path('quem-somos/', views.QuemSomosPage, name='quem_somos'),

]