import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Leccion

Leccion.objects.all().delete()

Leccion.objects.create(numero=1, titulo='Historia de AlCapone', youtube_id='D2W3CjuAjDw', orden=1)
Leccion.objects.create(numero=2, titulo='Código de Honor', youtube_id='O5-dlf_1jCY', orden=2)

print('✅ Lecciones cargadas correctamente')