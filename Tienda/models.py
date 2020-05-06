from django.db import models
from Catalogo.models import Producto
from Analitica.models import Zona

class Tienda( models.Model ):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=40, default='Sin nombre')
    ingresos = models.BigIntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=150, null=False, blank=False)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}'.format(self.nombre+" ("+self.direccion+")")

class Producto_inventario( models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return '{}'.format(self.producto.get_nombre()+" - "+self.cantidad)

class Venta(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    cedula_cliente = models.CharField(max_length=12, default="NA")
    fecha = models.DateField(auto_now=True)
    total = models.IntegerField(null=False, blank=False, default=0)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Producto_venta( models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    subtotal = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return '{}'.format(self.producto.get_nombre()+" - "+self.cantidad)

class Recordatorio(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre_cliente = models.CharField(max_length=40, default='Sin nombre')
    deuda = models.IntegerField(null=False, blank=False, default=0)
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_cliente+": $"+str(self.deuda))