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
    path('registro/', views.registro, name='registro'),

    # ── PERFIL ──
    path('perfil/', views.perfil, name='perfil'),
    path('cambiar-contrasena/', views.cambiar_contrasena, name='cambiar_contrasena'),

    # ── NOTICIAS ──
    path('noticias/<int:noticia_id>/', views.noticia_detalle, name='noticia_detalle'),

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

    # ── CONQUISTAS ──
    path('panel/conquista/nueva/', views.panel_conquista_nueva, name='panel_conquista_nueva'),
    path('panel/conquista/<int:conquista_id>/editar/', views.panel_conquista_editar, name='panel_conquista_editar'),
    path('panel/conquista/<int:conquista_id>/eliminar/', views.panel_conquista_eliminar, name='panel_conquista_eliminar'),

    # ── MULTIMEDIA ──
    path('panel/video/agregar/', views.panel_video_agregar, name='panel_video_agregar'),
    path('panel/video/<int:video_id>/eliminar/', views.panel_video_eliminar, name='panel_video_eliminar'),
    path('panel/foto/agregar/', views.panel_foto_agregar, name='panel_foto_agregar'),
    path('panel/foto/<int:foto_id>/eliminar/', views.panel_foto_eliminar, name='panel_foto_eliminar'),

    # ── LECCIONES ──
    path('panel/leccion/agregar/', views.panel_leccion_agregar, name='panel_leccion_agregar'),
    path('panel/leccion/<int:leccion_id>/eliminar/', views.panel_leccion_eliminar, name='panel_leccion_eliminar'),

    # ── PANEL NOTICIAS ──
    path('panel/noticia/agregar/', views.panel_noticia_agregar, name='panel_noticia_agregar'),
    path('panel/noticia/<int:noticia_id>/editar/', views.panel_noticia_editar, name='panel_noticia_editar'),
    path('panel/noticia/<int:noticia_id>/eliminar/', views.panel_noticia_eliminar, name='panel_noticia_eliminar'),

    # ── USUARIOS ──
    path('panel/usuario/<int:user_id>/desactivar/', views.panel_usuario_desactivar, name='panel_usuario_desactivar'),
    path('panel/usuario/<int:user_id>/eliminar/', views.panel_usuario_eliminar, name='panel_usuario_eliminar'),
    path('panel/usuario/<int:user_id>/permiso/', views.panel_usuario_permiso, name='panel_usuario_permiso'),

    # ── MANTENIMIENTO ──
    path('panel/mantenimiento/', views.panel_mantenimiento_toggle, name='panel_mantenimiento_toggle'),
]