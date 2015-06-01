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
			d.username = cd['username']
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
			username=cd['username']
			password=cd['password']

			user=authenticate(username=username, password=password)
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
	return render(request, 'login/play.html', {'score':details().team_points, 'que_data':score.objects.all(), 'form':play_form()} )

def play_qn(request, oye):
	a=int(oye)
	score=que_data

	if request.method=='POST':
		form=play_form(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			answer=cd['answer']
			ans=que_data.objects.get(qno=a)
			if answer == ans.ans:
				m=details().team_points+ans.points
				details().save()
				return HttpResponse('your score %s' % m )

			else:
				return HttpResponseRedirect('/play')

	else:
		try:
			x = que_data.objects.get(qno=a)
		except que_data.DoesNotExist:
			x = None
		return render(request, 'login/question.html', {'que':x.que, 'form':play_form(), 'score':details().team_points})#.points, 'q':score.objects.all(), 'a':a})#,"you r on question %s" % a)