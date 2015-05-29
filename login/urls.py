from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
	url(r'^register/', views.register),
	url(r'^$', views.login),
	url(r'^play/', views.play),
	)