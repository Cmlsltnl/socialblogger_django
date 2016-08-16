from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)

from .forms import UserLoginForm,UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
	print(request.user.is_authenticated())
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	title = "Login"
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password )
		print(request.user.is_authenticated())
		login(request,user)
		
		if next:
			return redirect(next)
		return redirect('/blog')

	return render(request,"form.html",{"form":form,"title":title,"notloggedin":1,"login":1})

def register_view(request):
	print(request.user.is_authenticated())
	next = request.GET.get('next')
	form = UserRegisterForm(request.POST or None)
	title = "register"
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()

		# we only use "new_user" varable so as to not confuse it with "user" varaible already used
		new_user = authenticate(username=user.username,password=password )
		login(request,new_user)
		
		if next:
			return redirect(next)
		return redirect('/')

	context = {"form":form,"title":title,"notloggedin":1,"register":1}

	return render(request,"form.html",context)


def logout_view(request):
	logout(request)
	
	return redirect('/')

















