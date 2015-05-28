from django.shortcuts import render
from login.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from login.models import details

# Create your views here.

def register(request):
	if request.method =="POST":
		form = register_form(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			d=details()
			d.member1 = cd['member1']
			d.member2 = cd['member2']
			d.email = cd['email']
			d.teamname = cd['teamname']
			d.password = cd['password']
			try:
				d.save()
			except:
				return HttpResponse("error")
			return HttpResponseRedirect('http://127.0.0.1:8000/')

		else:
			return HttpResponse("form invalid")

	else:
		form = register_form
	return render(request, 'login/register.html', {'form':form})
	#form = register_form()
	#return render(request, 'login/register.html', {'form':form})

def login(request):
	if request.method =="POST":
		form = login_form(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			d=details()
			try:
				d.teamname == cd['name_team']
				d.password == cd['password_login']
			except:
				return HttpResponse("error")
			return HttpResponse("ok... login succesful")
		else:
			return HttpResponse("invalid form")

	else:
		form = login_form()
	return render(request, 'login/login.html', {'form':form})

