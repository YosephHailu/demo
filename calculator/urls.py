from . import views
from django.urls import path

urlpatterns = [
    path('', views.calculator, name='calculate'),
    path('userRegister', views.userRegister, name="userRegister"),
    path('login', views.login_request, name="login"),

]