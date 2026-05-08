from django.db import models

class Era(models.Model):
    numero = models.IntegerField()
    periodo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    titulo_dorado = models.CharField(max_length=100)
    tagline = models.CharField(max_length=300)
    texto = models.TextField()

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return f"Era {self.numero} — {self.titulo}"


class Lider(models.Model):
    era = models.ForeignKey(Era, on_delete=models.CASCADE, related_name='lideres')
    avatar = models.CharField(max_length=5)
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.nombre


class Victoria(models.Model):
    era = models.ForeignKey(Era, on_delete=models.CASCADE, related_name='victorias')
    nombre = models.CharField(max_length=200)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.nombre


class Tag(models.Model):
    era = models.ForeignKey(Era, on_delete=models.CASCADE, related_name='tags')
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Estadistica(models.Model):
    era = models.ForeignKey(Era, on_delete=models.CASCADE, related_name='estadisticas')
    numero = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.numero} — {self.label}"


class Conquista(models.Model):
    METODO_CHOICES = [
        ('Persuasión', 'Persuasión'),
        ('Infiltración', 'Infiltración'),
        ('Engaño', 'Engaño'),
        ('Trampa', 'Trampa'),
        ('Oferta monetaria', 'Oferta monetaria'),
    ]
    anio = models.IntegerField()
    organizacion = models.CharField(max_length=200)
    guerreros = models.CharField(max_length=300)
    metodo = models.CharField(max_length=50, choices=METODO_CHOICES)

    class Meta:
        ordering = ['-anio']

    def __str__(self):
        return f"{self.anio} — {self.organizacion}"


class VideoMultimedia(models.Model):
    titulo = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=20)
    anio = models.IntegerField()
    descripcion = models.CharField(max_length=300, blank=True)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden', '-anio']

    def __str__(self):
        return f"{self.titulo} ({self.anio})"


class FotoMultimedia(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='multimedia/fotos/')
    anio = models.IntegerField()
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden', '-anio']

    def __str__(self):
        return f"{self.titulo} ({self.anio})"


class Leccion(models.Model):
    numero = models.IntegerField()
    titulo = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=20)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden', 'numero']

    def __str__(self):
        return f"Lección {self.numero} — {self.titulo}"