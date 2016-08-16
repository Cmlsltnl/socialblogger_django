from django.db import models
# from accounts.models import User
from django.core.urlresolvers import reverse
# Create your models here.
# from django.contrib.auth import (
	# authenticate,
	# get_user_model,
	# login,
	# logout
	# ) 

# User = get_user_model()
# from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	# user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	user = models.ForeignKey(User,default=1)
	likes = models.IntegerField(blank=True,null=True)
	file_field = models.FileField(blank=True,null=True)
	created_on = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True,null=True)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('blog-detail', kwargs={'pk': self.pk})



# class Comment(models.Model):
	
# 	text = models.TextField()
# 	post = models.ForeignKey(Post)
# 	created_on = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
# 	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)


# 	def __str__(self):
# 		return self.title



# from django.core.urlresolvers import reverse
# from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_length=200)

#     def get_absolute_url(self):
#         return reverse('author-detail', kwargs={'pk': self.pk})
