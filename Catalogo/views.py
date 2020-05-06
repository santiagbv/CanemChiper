from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Producto


def catalogo(request):

    obj = Producto.objects.get(id=1)
    context={
        "data":obj
    }
    return render(request, 'catalogo.html', context)