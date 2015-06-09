from django.shortcuts import render
from login.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from login.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.

def register(request):
	if request.method =="POST":
		form = register_form(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			d=details()
			u=User()
			d.member1 = cd['member1']
			d.member2 = cd['member2']
			d.email = cd['email']
			u.username = cd['username']
			u.set_password(cd['password'])
			u.email=cd['email']
			
			try:
				u.save()
			except:
				return HttpResponse("error")
			d.user=u
			d.save()
			

			return HttpResponseRedirect('/')#'http://127.0.0.1:8000/')

		else:
			return HttpResponse("form invalid")

	else:
		form = register_form
	return render(request, 'login/register.html', {'form':form})
	#form = register_form()
	#return render(request, 'login/register.html', {'form':form})

def login(request):
#	if request.user.is_authenticated():
#		return HttpResponseRedirect('/')	
	if request.method =="POST":
		form = login_form(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			d=details()
			username=cd['username']
			password=cd['password']

			user=authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					return HttpResponseRedirect("/play")
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

@login_required
def play(request):
	u=request.user

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
		us=details.objects.get(user=u)
	return render(request, 'login/play.html', {'score':us.team_points, 'que_data':score.objects.all(), 'form':play_form()} )

@login_required
def play_qn(request, num):
	a=int(num)
	score=que_data

	if request.method=='POST':
		form=play_form(request.POST)
		u=request.user
		team=details.objects.get(user=u)
		if form.is_valid():
			cd=form.cleaned_data
			answer=cd['answer']
			ans=que_data.objects.get(qno=a)
			if answer == ans.ans:
				team.team_points+=ans.points
				team.save()
				return HttpResponseRedirect('/play')

			else:
				return HttpResponseRedirect('/play')

	else:
		try:
			x = que_data.objects.get(qno=a)
		except que_data.DoesNotExist:
			x = None
		u=request.user
		d=details.objects.get(user=u)			
		return render(request, 'login/question.html', {'que':x.que, 'form':play_form(), 'score':d.team_points})#.points, 'q':score.objects.all(), 'a':a})#,"you r on question %s" % a)

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('http://127.0.0.1:8000')