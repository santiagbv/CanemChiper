from django.db import models

class Producto(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=25, default='Sin nombre')
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200, default='Sin descripción')
    categoria = models.CharField(max_length=25, default='Sin categoría')

    def __str__(self):
        return self.nombre

    def get_nombre(self):
        return self.nombre


class Descuento(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    inicio = models.DateField(auto_now=False, auto_now_add=False)
    fin = models.DateField(auto_now=False, auto_now_add=False)
    porcentaje = models.DecimalField(max_digits=2, decimal_places=2)
    ciudad = models.CharField(max_length=30)

    def __str__(self):
        porc = str(self.porcentaje*100)
        return '{}'.format(self.producto.get_nombre() + " " +porc+ "%")
