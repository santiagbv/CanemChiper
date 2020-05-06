from django.contrib import admin
from .models import Tienda, Venta, Producto_inventario, Producto_venta, Recordatorio

# Register your models here.
admin.site.register(Tienda)
admin.site.register(Venta)
admin.site.register(Producto_inventario)
admin.site.register(Producto_venta)
admin.site.register(Recordatorio)
