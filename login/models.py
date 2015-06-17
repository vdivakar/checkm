from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
 


# Create your models here.
class details(models.Model):
	member1 = models.CharField(max_length=100)
	member2 = models.CharField(max_length = 100)
	email = models.EmailField()
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	user=models.ForeignKey(User,unique=True)#, default=4)#extending user model
	team_points=models.IntegerField(default=0)
	#answer=models.ForeignKey('answered')#, unique=False , blank=True, null=True,)

	def __unicode__(self):
		return self.user.username

	class Meta:
		ordering =['username']


class que_data(models.Model):
	qno = models.IntegerField()
	que= models.CharField(max_length=100)
	ans = models.CharField(max_length=100)
	points=models.IntegerField(default=100)
	lock=models.IntegerField(default=0)

	def __unicode__(self):
		#qno="qno"
		return self.que
	class Meta:
		ordering=['qno']

class answered(models.Model):
	attempt=models.IntegerField(default=10000)# que. no. attempted
	who=models.CharField(max_length=100, default="hey")# name of the team who attempted

	def __unicode__(self):
		return self.who

admin.site.register(details)
admin.site.register(que_data)
admin.site.register(answered)
