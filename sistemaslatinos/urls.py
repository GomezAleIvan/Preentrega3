"""
URL configuration for sistemaslatinos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import  LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludar),
    path("edad/<int:edad>" , views.mayor_edad),
    path("template", views.probando_template),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path("logout", LogoutView. as_view(template_name="logout.html") , name="Logout")
]

