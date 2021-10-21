from os import name
from django.contrib import admin
from django.urls import path
from usuarios.views import index
from visitantes.views import registrar_visitantes

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        '', 
        index,
        name = 'index'
    ),

    path(
        'register',
        registrar_visitantes,
        name='registrar_visitantes'
    )
]
