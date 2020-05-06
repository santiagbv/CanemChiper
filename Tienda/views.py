from django.shortcuts import render
from django.shortcuts import HttpResponse

def Tienda(request):
    return HttpResponse("<h1>Bienvenido a tú tienda<h1>")
