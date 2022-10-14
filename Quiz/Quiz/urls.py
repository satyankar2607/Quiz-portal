"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup', views.signup, name='sigup'),
    path('login', views.login, name='login'),
    path('logch', views.logch, name='logch'),
    path('adm', views.adm, name='adm'),
    path('add', views.add, name='add'),
    path('dele', views.dele, name='dele'),
    path('showquestions', views.showquestions, name='showquestions'),
    path('user', views.user, name='user'),
    path('calc', views.calc, name='calc'),
    path('public_leaderboard', views.public_leaderboard, name='public_leaderboard'),


]
