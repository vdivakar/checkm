from django import forms

class register_form(forms.Form):
	member1 = forms.CharField(max_length=100, label='member1')
	member2 = forms.CharField(max_length = 100, label='member2')
	email = forms.EmailField(required = True, label='email')
	teamname = forms.CharField(max_length=100, label='teamname')
	password = forms.CharField(widget=forms.PasswordInput(), label='password')

class login_form(forms.Form):
	name_team = forms.CharField()
	password_login = forms.CharField(widget=forms.PasswordInput())

class play_form(forms.Form):
	answer=forms.CharField(required=False)