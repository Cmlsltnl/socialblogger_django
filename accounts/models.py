from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# class User(models.Model):
# 	user = models.OneToOneField(User,default="")
# 	username = models.CharField(max_length=140,unique=True)
# 	email = models.EmailField(max_length=140,unique=True)
	
# 	def __str__(self):
# 		return self.username	







# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)

# 	def __str__(self):
# 		return self.user.username