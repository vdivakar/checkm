from django.db import models
from django.contrib import admin


# Create your models here.
class details(models.Model):
	member1 = models.CharField(max_length=100)
	member2 = models.CharField(max_length = 100)
	email = models.EmailField()
	teamname = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

	def __unicode__(self):
		return self.teamname

	class Meta:
		ordering =['teamname']


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

