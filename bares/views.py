from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index (request):
	return HttpResponse ("Hola desde bares")

def registro (request):
	return HttpResponse ("Esto es el registro")

def registroFulanito (request, fulanito):
	return HttpResponse ("Registro de %s" % fulanito)

def web (request, fulanito):
	context = {"fulanito":fulanito}
	return render(request, 'index.html', context)