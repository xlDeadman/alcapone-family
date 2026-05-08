from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Era, Lider, Victoria, Tag, Estadistica

def inicio(request):
    return render(request, 'index.html')

def historia(request):
    eras = Era.objects.prefetch_related('lideres', 'victorias', 'tags', 'estadisticas').all()
    return render(request, 'historia.html', {'eras': eras})

def historia_belica(request):
    return render(request, 'historia-belico.html')

def contador_petadas(request):
    return render(request, 'contador-petadas.html')

def multimedia_petadas(request):
    return render(request, 'multimedia-petadas.html')

def chicago_school(request):
    return render(request, 'chicago-school.html')

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
    return render(request, 'panel/panel.html', {
        'eras': eras,
        'total_lideres': total_lideres,
        'total_victorias': total_victorias,
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