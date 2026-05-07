from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def historia(request):
    return render(request, 'historia.html')

def historia_belica(request):
    return render(request, 'historia-belico.html')

def contador_petadas(request):
    return render(request, 'contador-petadas.html')