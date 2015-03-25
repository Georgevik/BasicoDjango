from django.conf.urls import patterns, url

from bares import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name='index'),
	url(r'^registro$', views.registro, name='registro'),
	url(r'^web_(?P<fulanito>\w+)/$', views.web, name='web'),
	url(r'^registro_de(?P<fulanito>\w+)/$', views.registroFulanito, name='registroFulanito'),
)