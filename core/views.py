from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from core.models import Era, Lider, Victoria, Tag, Estadistica, Conquista, VideoMultimedia, FotoMultimedia, Leccion

def inicio(request):
    return render(request, 'index.html')

def historia(request):
    eras = Era.objects.prefetch_related('lideres', 'victorias', 'tags', 'estadisticas').all()
    return render(request, 'historia.html', {'eras': eras})

def historia_belica(request):
    conquistas = Conquista.objects.all()
    return render(request, 'historia-belico.html', {'conquistas': conquistas})

def contador_petadas(request):
    familias = Conquista.objects.values('organizacion').annotate(
        total=Count('id')
    ).order_by('-total', 'organizacion')
    total_pettadas = Conquista.objects.count()
    total_familias = familias.count()
    con_multiple = familias.filter(total__gte=2).count()
    max_total = familias.first()['total'] if familias.exists() else 1
    return render(request, 'contador-petadas.html', {
        'familias': familias,
        'total_pettadas': total_pettadas,
        'total_familias': total_familias,
        'con_multiple': con_multiple,
        'max_total': max_total,
    })

def multimedia_petadas(request):
    videos = VideoMultimedia.objects.all()
    fotos = FotoMultimedia.objects.all()
    return render(request, 'multimedia-petadas.html', {
        'videos': videos,
        'fotos': fotos,
    })

def chicago_school(request):
    lecciones = Leccion.objects.all()
    return render(request, 'chicago-school.html', {'lecciones': lecciones})

def codigos(request):
    return render(request, 'codigos.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, user.username)
            return redirect('inicio')
        else:
            return render(request, 'login.html', {'error': True})
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

# ── PANEL ──
@login_required
def panel(request):
    eras = Era.objects.prefetch_related('lideres', 'victorias', 'tags').all()
    total_lideres = sum(era.lideres.count() for era in eras)
    total_victorias = sum(era.victorias.count() for era in eras)
    conquistas = Conquista.objects.all()
    total_conquistas = conquistas.count()
    conquistas_persuasion = conquistas.filter(metodo='Persuasión').count()
    conquistas_infiltracion = conquistas.filter(metodo='Infiltración').count()
    conquistas_otros = conquistas.exclude(metodo__in=['Persuasión', 'Infiltración']).count()
    conquistas_familias = conquistas.values('organizacion').distinct().count()
    conquistas_multiple = conquistas.values('organizacion').annotate(total=Count('id')).filter(total__gte=2).count()
    top_familias = conquistas.values('organizacion').annotate(total=Count('id')).order_by('-total')[:8]
    videos = VideoMultimedia.objects.all()
    fotos = FotoMultimedia.objects.all()
    lecciones = Leccion.objects.all()
    return render(request, 'panel/panel.html', {
        'eras': eras,
        'total_lideres': total_lideres,
        'total_victorias': total_victorias,
        'conquistas': conquistas,
        'total_conquistas': total_conquistas,
        'conquistas_persuasion': conquistas_persuasion,
        'conquistas_infiltracion': conquistas_infiltracion,
        'conquistas_otros': conquistas_otros,
        'conquistas_familias': conquistas_familias,
        'conquistas_multiple': conquistas_multiple,
        'top_familias': top_familias,
        'videos': videos,
        'fotos': fotos,
        'lecciones': lecciones,
    })

# ── ERA ──
@login_required
def panel_era_nueva(request):
    if request.method == 'POST':
        era = Era.objects.create(
            numero=Era.objects.count() + 1,
            periodo=request.POST.get('periodo'),
            titulo=request.POST.get('titulo'),
            titulo_dorado=request.POST.get('titulo_dorado'),
            tagline=request.POST.get('tagline'),
            texto=request.POST.get('texto'),
        )
        return redirect('panel_era_editar', era_id=era.id)
    return render(request, 'panel/era_nueva.html')

@login_required
def panel_era_editar(request, era_id):
    era = get_object_or_404(Era, id=era_id)
    if request.method == 'POST':
        era.periodo = request.POST.get('periodo')
        era.titulo = request.POST.get('titulo')
        era.titulo_dorado = request.POST.get('titulo_dorado')
        era.tagline = request.POST.get('tagline')
        era.texto = request.POST.get('texto')
        era.save()
        messages.success(request, 'era_guardada')
        return redirect('panel_era_editar', era_id=era.id)
    return render(request, 'panel/era_editar.html', {'era': era})

# ── LÍDERES ──
@login_required
def panel_lider_agregar(request, era_id):
    era = get_object_or_404(Era, id=era_id)
    if request.method == 'POST':
        Lider.objects.create(
            era=era,
            avatar=request.POST.get('avatar'),
            nombre=request.POST.get('nombre'),
            rol=request.POST.get('rol'),
            orden=era.lideres.count() + 1
        )
    return redirect('panel_era_editar', era_id=era_id)

@login_required
def panel_lider_eliminar(request, lider_id):
    lider = get_object_or_404(Lider, id=lider_id)
    era_id = lider.era.id
    lider.delete()
    return redirect('panel_era_editar', era_id=era_id)

# ── VICTORIAS ──
@login_required
def panel_victoria_agregar(request, era_id):
    era = get_object_or_404(Era, id=era_id)
    if request.method == 'POST':
        Victoria.objects.create(
            era=era,
            nombre=request.POST.get('nombre'),
            orden=era.victorias.count() + 1
        )
    return redirect('panel_era_editar', era_id=era_id)

@login_required
def panel_victoria_eliminar(request, victoria_id):
    victoria = get_object_or_404(Victoria, id=victoria_id)
    era_id = victoria.era.id
    victoria.delete()
    return redirect('panel_era_editar', era_id=era_id)

# ── TAGS ──
@login_required
def panel_tag_agregar(request, era_id):
    era = get_object_or_404(Era, id=era_id)
    if request.method == 'POST':
        Tag.objects.create(era=era, nombre=request.POST.get('nombre'))
    return redirect('panel_era_editar', era_id=era_id)

@login_required
def panel_tag_eliminar(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    era_id = tag.era.id
    tag.delete()
    return redirect('panel_era_editar', era_id=era_id)

# ── ESTADÍSTICAS ──
@login_required
def panel_stat_agregar(request, era_id):
    era = get_object_or_404(Era, id=era_id)
    if request.method == 'POST':
        Estadistica.objects.create(
            era=era,
            numero=request.POST.get('numero'),
            label=request.POST.get('label'),
            orden=era.estadisticas.count() + 1
        )
    return redirect('panel_era_editar', era_id=era_id)

@login_required
def panel_stat_eliminar(request, stat_id):
    stat = get_object_or_404(Estadistica, id=stat_id)
    era_id = stat.era.id
    stat.delete()
    return redirect('panel_era_editar', era_id=era_id)

# ── CONQUISTAS ──
@login_required
def panel_conquista_nueva(request):
    if request.method == 'POST':
        Conquista.objects.create(
            anio=request.POST.get('anio'),
            organizacion=request.POST.get('organizacion'),
            guerreros=request.POST.get('guerreros'),
            metodo=request.POST.get('metodo'),
        )
        return redirect('panel')
    return render(request, 'panel/conquista_form.html', {
        'conquista': None,
        'metodo_choices': Conquista.METODO_CHOICES,
    })

@login_required
def panel_conquista_editar(request, conquista_id):
    conquista = get_object_or_404(Conquista, id=conquista_id)
    if request.method == 'POST':
        conquista.anio = request.POST.get('anio')
        conquista.organizacion = request.POST.get('organizacion')
        conquista.guerreros = request.POST.get('guerreros')
        conquista.metodo = request.POST.get('metodo')
        conquista.save()
        return redirect('panel')
    return render(request, 'panel/conquista_form.html', {
        'conquista': conquista,
        'metodo_choices': Conquista.METODO_CHOICES,
    })

@login_required
def panel_conquista_eliminar(request, conquista_id):
    conquista = get_object_or_404(Conquista, id=conquista_id)
    conquista.delete()
    return redirect('panel')

# ── VIDEOS ──
@login_required
def panel_video_agregar(request):
    if request.method == 'POST':
        VideoMultimedia.objects.create(
            titulo=request.POST.get('titulo'),
            youtube_id=request.POST.get('youtube_id'),
            anio=request.POST.get('anio'),
            descripcion=request.POST.get('descripcion', ''),
            orden=VideoMultimedia.objects.count() + 1
        )
        return redirect('panel')
    return redirect('panel')

@login_required
def panel_video_eliminar(request, video_id):
    video = get_object_or_404(VideoMultimedia, id=video_id)
    video.delete()
    return redirect('panel')

# ── FOTOS ──
@login_required
def panel_foto_agregar(request):
    if request.method == 'POST':
        FotoMultimedia.objects.create(
            titulo=request.POST.get('titulo'),
            imagen=request.FILES.get('imagen'),
            anio=request.POST.get('anio'),
            orden=FotoMultimedia.objects.count() + 1
        )
        return redirect('panel')
    return redirect('panel')

@login_required
def panel_foto_eliminar(request, foto_id):
    foto = get_object_or_404(FotoMultimedia, id=foto_id)
    foto.imagen.delete()
    foto.delete()
    return redirect('panel')

# ── LECCIONES ──
@login_required
def panel_leccion_agregar(request):
    if request.method == 'POST':
        Leccion.objects.create(
            numero=Leccion.objects.count() + 1,
            titulo=request.POST.get('titulo'),
            youtube_id=request.POST.get('youtube_id'),
            orden=Leccion.objects.count() + 1
        )
        return redirect('panel')
    return redirect('panel')

@login_required
def panel_leccion_eliminar(request, leccion_id):
    leccion = get_object_or_404(Leccion, id=leccion_id)
    leccion.delete()
    return redirect('panel')