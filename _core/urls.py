"""_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from materials.views import home_view_material, detail_view_material, tagged_material, upload_view_material, landing
from informatika.views import home_view_informatika, detail_view_informatika, tagged_informatika, upload_view_informatika

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    # Qanun
    path('qanun/', home_view_material, name="home_material"),
    path('qanun/privatupload/', upload_view_material, name="privatupload"),
    path('qanun/material/<slug:slug>/', detail_view_material, name="material"),
    path('qanun/derece/<slug:slug>/', tagged_material, name="tagged_material"),
    # Informatika
    path('informatika/', home_view_informatika, name="home_informatika"),
    path('informatika/privatupload/', upload_view_informatika, name="privatupload"),
    path('informatika/informatika/<slug:slug>/', detail_view_informatika, name="informatika"),
    path('informatika/derece/<slug:slug>/', tagged_informatika, name="tagged_informatika"),
]
