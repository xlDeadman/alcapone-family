from django.db import models

class Era(models.Model):
    numero = models.IntegerField()  # 1, 2, 3, 4, 5
    periodo = models.CharField(max_length=100)  # "2008 — 2011"
    titulo = models.CharField(max_length=200)  # "Era Antigua"
    titulo_dorado = models.CharField(max_length=100)  # "Antigua"
    tagline = models.CharField(max_length=300)
    texto = models.TextField()  # párrafos principales

    class Meta:
        ordering = ['numero']

    def __str__(self):
        return f"Era {self.numero} — {self.titulo}"


class Lider(models.Model):
    era = models.ForeignKey(Era, on_delete=models.CASCADE, related_name='lideres')
    avatar = models.CharField(max_length=5)   # "AC", "JP"
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
    numero = models.CharField(max_length=20)   # "12", "A.R.M", "∞"
    label = models.CharField(max_length=100)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.numero} — {self.label}"