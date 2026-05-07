from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),

    path('historia/', views.historia, name='historia'),

    path('historia-belico/', views.historia_belica, name='historia_belica'),

    path('admin/', admin.site.urls),

    path('contador-petadas/', views.contador_petadas, name='contador_petadas'),

]