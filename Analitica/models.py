from django.db import models
from Catalogo.models import Producto

class Zona(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=25, default='Sin nombre')
    ciudad = models.CharField(max_length=25, default='Sin nombre')
    pais = models.CharField(max_length=25, default='Sin nombre')

    def __str__(self):
        return '{}'.format(self.nombre+", "+self.ciudad+", "+self.pais)

    def get_nombre(self):
        return self.nombre

class Reporte(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    fecha = models.DateField(auto_now=True)
    descripcion =  models.CharField(max_length=80, default="NA")
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE , null = False , default=None)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return '{}'.format(self.zona.get_nombre()+" - "+self.fecha)