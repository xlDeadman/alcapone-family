import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import FotoMultimedia

# Limpiar fotos previas
FotoMultimedia.objects.all().delete()

carpeta = 'media/multimedia/fotos/'
archivos = os.listdir(carpeta)
imagenes = [f for f in archivos if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]

for i, imagen in enumerate(sorted(imagenes)):
    FotoMultimedia.objects.create(
        titulo=f'Pettada {i+1}',
        imagen=f'multimedia/fotos/{imagen}',
        anio=2024,
        orden=i+1
    )
    print(f'✅ {imagen}')

print(f'\n✅ {len(imagenes)} fotos cargadas correctamente')