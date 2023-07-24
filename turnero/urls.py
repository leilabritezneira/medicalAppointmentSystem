"""turnero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login_views, name='login'),
    path('index/', views.Index, name='turnero'),
    path('persona/', views.Persona_views, name='persona'),
    path('servicio/', views.Servicio_views, name='servicio'),
    path('turnos/', views.Turnos_views, name='turnos'),
    path('lista_servicios/', views.ListaServicios_views, name='lista_servicios'),
    path('lista_turnos/', views.ListaTurnos_views, name='lista_turnos'),
    path('lista_personas/', views.ListaPersonas_views, name='lista_personas')
]
urlpatterns += staticfiles_urlpatterns()

#para definicion de migracion de archivos de nuestro proyecto a nuestro servidor de archivos (static_env)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)