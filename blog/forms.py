# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField()
#     message = forms.CharField(widget=forms.Textarea)

#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # name = forms.CharField()
    # body = forms.CharField(widget=forms.Textarea)

    class Meta:
    	model = Post
    	fields = ['title',
  		  	'body',
    		'file_field'
    	]
        
        # widgets = {
        #     'body' : forms.Textarea(attrs={'rows':4, 'cols':15})
        # }

    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary
    	# pass


# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ['text',

#         ]




