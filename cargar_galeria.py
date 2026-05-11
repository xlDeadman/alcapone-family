import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import FotoGaleria

carpeta = r'C:\Users\Alan Romero\Desktop\Multimedia'

archivos = [f for f in os.listdir(carpeta) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp'))]

for i, archivo in enumerate(sorted(archivos)):
    ruta = os.path.join(carpeta, archivo)
    nombre = os.path.splitext(archivo)[0]
    with open(ruta, 'rb') as f:
        from django.core.files import File
        foto = FotoGaleria(titulo=nombre, orden=i+1)
        foto.imagen.save(archivo, File(f), save=True)
    print(f'✓ {archivo}')

print(f'\nListo — {len(archivos)} fotos cargadas.')