from django.shortcuts import render,redirect
from django import forms
from django.core.validators import validate_slug, RegexValidator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

from django.http import HttpResponse

def index (request):
	return render (request, 'index.html', {})

def bienvenido (request):
	return render (request, 'bienvenido.html', {})

class registroForm(forms.Form):
	name = forms.CharField (label      = 'Nombre', 
							max_length = 10, 
							required   = True,)

	email = forms.CharField (label      = 'Su correo', 
							max_length = 10, 
							required   = True,)

	password = forms.CharField (label      = 'Password', 
							max_length = 10,
							widget=forms.PasswordInput,
							required   = True,)
	def clean (self):
		cleaned_data = super(registroForm, self).clean()
					

class loginForm(forms.Form):
	nombre = forms.CharField (	label      = 'Nombre', 
								max_length = 10, 
								required   = True,)
							
	password = forms.CharField(	label		= 'Password',
								required 	= True,
								widget		= forms.PasswordInput,)

	def clean (self):
		cleaned_data = super(loginForm, self).clean()

def logoutController(request):
	logout(request)
	return redirect('bienvenido')

def loginController(request):
	if request.method == 'POST':

		#Obtenemos el form del post
		form = loginForm (request.POST)

		if form.is_valid ():
			user = authenticate(username 	= form.cleaned_data['nombre'], 
								password	= form.cleaned_data['password'])
				
			if user is not None:
				#si el usuario esta activo ya
				if user.is_active:
					login(request, user)
					return redirect ('bienvenido')

				#Si el usuario no esta activo
				else:
					context = {
						'mensaje':'Usuario no activo',
						'form':form,
					}
					return render (request, 'login.html', context)

			#Ese usuario no esta registrado	
			else:
				form = loginForm()

				context = {
					'mensaje':'Usuario o contrasena incorrecta',
					'form':form,
				}
				return render (request, 'login.html',context)
				
		#si lo dejo en blanco
		else:
			context = {
				'mensaje':'Rellena troll',
				'form':form,
			}

			return render (request, 'login.html',context)



	#Es la primera vez que se llama al metodo
	else:
		form = loginForm()

		context = {
			'mensaje':'Loguase en la aplicacion',
			'form':form,
		}
		return render (request, 'login.html', context)


def formulario (request):
	# Recibo el formulario
	if request.method == 'POST':

		# bound data to form
		form = registroForm (request.POST)

		if form.is_valid ():
			context =  {
				'fulanito':form.cleaned_data['name'],
				'form':form,
			}
			user = User.objects.create_user(form.cleaned_data['name'],
											form.cleaned_data['email'],
											form.cleaned_data['password'])
			user.save()


			return render (request, 'login.html', context)


		else:
			context =  {
				'fulanito': 'error',
				'form':form,
			}

			return render (request, 'registro.html', context)
	# Entrando la primera vez desde GET
	else:
		fulanito = 'default'

		form = registroForm ()

		context = {
			'fulanito':fulanito,
			'form':form,
		}
		return render (request, 'registro.html',context)











