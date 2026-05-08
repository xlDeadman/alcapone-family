from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('historia/', views.historia, name='historia'),
    path('historia-belico/', views.historia_belica, name='historia_belica'),
    path('admin/', admin.site.urls),
    path('contador-petadas/', views.contador_petadas, name='contador_petadas'),
    path('historia-belico/multimedia/', views.multimedia_petadas, name='multimedia_petadas'),
    path('chicago-school/', views.chicago_school, name='chicago_school'),
    path('codigos/', views.codigos, name='codigos'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # ── PANEL ──
    path('panel/', views.panel, name='panel'),
    path('panel/era/nueva/', views.panel_era_nueva, name='panel_era_nueva'),
    path('panel/era/<int:era_id>/', views.panel_era_editar, name='panel_era_editar'),
    path('panel/era/<int:era_id>/lider/agregar/', views.panel_lider_agregar, name='panel_lider_agregar'),
    path('panel/lider/<int:lider_id>/eliminar/', views.panel_lider_eliminar, name='panel_lider_eliminar'),
    path('panel/era/<int:era_id>/victoria/agregar/', views.panel_victoria_agregar, name='panel_victoria_agregar'),
    path('panel/victoria/<int:victoria_id>/eliminar/', views.panel_victoria_eliminar, name='panel_victoria_eliminar'),
    path('panel/era/<int:era_id>/tag/agregar/', views.panel_tag_agregar, name='panel_tag_agregar'),
    path('panel/tag/<int:tag_id>/eliminar/', views.panel_tag_eliminar, name='panel_tag_eliminar'),
    path('panel/era/<int:era_id>/stat/agregar/', views.panel_stat_agregar, name='panel_stat_agregar'),
    path('panel/stat/<int:stat_id>/eliminar/', views.panel_stat_eliminar, name='panel_stat_eliminar'),
]