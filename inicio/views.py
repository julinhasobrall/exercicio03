from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def soma(request, a, b):
    resultado = a + b
    return HttpResponse(f"A soma de {a} + {b} é: {resultado}")