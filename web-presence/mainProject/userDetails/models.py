from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class memberDetails(models.Model):
	memberName=models.CharField('Full Name', max_length=100)
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	memberGender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES)
	memberLocation=models.CharField('Location',max_length=100)
	memberContactNumber=models.IntegerField('Contact Number',max_length=14)
	memberAge=models.IntegerField('Age',max_length=3)
	memberEmail=models.EmailField('Email ID', max_length=100)
	memberRegistrationDate=models.DateTimeField('Registration Date')
	memberOccupation=models.CharField('Occupation',max_length=100)
	memberUserNumber=models.ForeignKey(User, unique=True)

	def __str__(self):
		return str(self.memberUserNumber)

class memberSocialNetworks(models.Model):
	facebook=models.CharField('Facebook',max_length=100)
	twitter=models.CharField('Twitter',max_length=100)
	linkedin=models.CharField('LinkedIn',max_length=100)
	github=models.CharField('Github',max_length=100)
	googleplus=	models.CharField('GooglePlus',max_length=100)
	stackoverflow=models.CharField('Stackoverflow',max_length=100)
	memberUserNumber=models.ForeignKey(User, unique=True)

	def __str__(self):
		return str(self.memberUserNumber)