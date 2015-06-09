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

	def __unicode__(self):
		return self.user.username

	class Meta:
		ordering =['username']


class que_data(models.Model):
	qno = models.IntegerField()
	que= models.CharField(max_length=100)
	ans = models.CharField(max_length=100)
	points=models.IntegerField(default=100)

	def __unicode__(self):
		#qno="qno"
		return self.que
	class Meta:
		ordering=['qno']

admin.site.register(details)
admin.site.register(que_data)

