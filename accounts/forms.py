from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	) 

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user is no longer active")
		return super(UserLoginForm,self).clean(*args,**kwargs)
		

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email address')
	email2 = forms.EmailField(label='Confirm email address')
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput,label='confirm password')

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',
			'password2',
		]

	#it matters that  the following method is clean_email2 and not clean_email since the last field out of the 2 is email2.
	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")
		if email!=email2:
			raise forms.ValidationError("emails must match")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise ValidationError("This email already exists")
		return email

	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password!=password2:
			raise forms.ValidationError("password must match")
		return password
