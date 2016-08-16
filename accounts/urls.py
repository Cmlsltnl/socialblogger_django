from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import ListView,DetailView
from .models import User
from accounts.views import (login_view,register_view,logout_view)

urlpatterns = [
   
	url(r'^login/',login_view,name='login'),
    url(r'^logout/',logout_view,name='logout'),
    url(r'^register/',register_view,name='register'),
]




