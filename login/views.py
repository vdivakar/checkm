from django.shortcuts import render
from login.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from login.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

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
			teamname=cd['name_team']
			password=cd['password_login']

			user=authenticate(username=teamname, password=password)
			if user is not None:
				return HttpResponse("correct")
			else:
				return HttpResponse("wrong")
			'''for d in details.objects:
				if d.teamname == cd['name_team']:
					 if d.password == cd['password_login']:
					 	return HttpResponse("ok... login succesful")
					 else:
					 	return HttpResponse("error1")
				else:
					return HttpResponse("error2")'''

			'''try:
				d.teamname == cd['name_team'] 
				try:
					d.password == cd['password_login']
				#d.password == cd['password_login']
				except:
					return HttpResponse("error 2")
			except:
				return HttpResponse("error")
			return HttpResponse("ok... login succesful")'''
		else:
			return HttpResponse("invalid form")

	else:
		form = login_form()
	return render(request, 'login/login.html', {'form':form})


def play(request):
	if request.method=='POST':
		form=play_form(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			answer=cd['answer']
		else:
			return HttpResponse("invalid0")
		return HttpResponse("ok")

	else:
		score=que_data
	return render(request, 'login/play.html', {'score':score().points, 'que_data':score.objects.all(), 'form':play_form()} )