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

admin.site.register(details)

