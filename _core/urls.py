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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from materials.views import home_view_material, detail_view_material, tagged_material, upload_view_material, landing
from informatika.views import home_view_informatika, detail_view_informatika, tagged_informatika, upload_view_informatika
from azdili.views import home_view_azdili, detail_view_azdili, tagged_azdili, upload_view_azdili
from mentiq.views import home_view_mentiq, detail_view_mentiq, tagged_mentiq, upload_view_mentiq

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    # Qanun
    path('qanunvericilik/', home_view_material, name="home_material"),
    path('qanunvericilik/privatupload/', upload_view_material, name="privatupload_material"),
    path('qanunvericilik/<slug:slug>/', detail_view_material, name="material"),
    path('qanunvericilik/derece/<slug:slug>/', tagged_material, name="tagged_material"),
    # Informatika
    path('informatika/', home_view_informatika, name="home_informatika"),
    path('informatika/privatupload/', upload_view_informatika, name="privatupload_informatika"),
    path('informatika/<slug:slug>/', detail_view_informatika, name="informatika"),
    path('informatika/derece/<slug:slug>/', tagged_informatika, name="tagged_informatika"),
    #Azərbaycan dili
    path('azerbaijan-dili/', home_view_azdili, name="home_azdili"),
    path('azerbaijan-dili/privatupload/', upload_view_azdili, name="privatupload_azdili"),
    path('azerbaijan-dili/<slug:slug>/', detail_view_azdili, name="azdili"),
    path('azerbaijan-dili/derece/<slug:slug>/', tagged_azdili, name="tagged_azdili"),
    #Mentiq dili
    path('mentiq/', home_view_mentiq, name="home_mentiq"),
    path('mentiq/privatupload/', upload_view_mentiq, name="privatupload_mentiq"),
    path('mentiq/<slug:slug>/', detail_view_mentiq, name="mentiq"),
    path('mentiq/derece/<slug:slug>/', tagged_mentiq, name="tagged_mentiq"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)