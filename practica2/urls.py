from django.conf.urls import patterns, url

from practica2 import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name='index'),
	url(r'^registro$', views.formulario, name='registro'),
	url(r'^bienvenido$', views.bienvenido, name='bienvenido'),
	url(r'^login$', views.loginController, name='loginController'),
	url(r'^logout$', views.logoutController, name='logoutController'),
)