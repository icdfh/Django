from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category is empty"

    class Meta:
        model = Support
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Length is bigger 200')

        return title


class RegisterUserForm(UserCreationForm):
   username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-group', 'placeholder':'Login'}))
   email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-group' , 'placeholder':'Email'}))
   password1 = forms.CharField(label='Passwords', widget=forms.PasswordInput(attrs={'class': 'form-group' , 'placeholder':'Enter ur password'}))
   password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-group',  'placeholder':'Re password'}))

   class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-group','placeholder':'Enter username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-group ','placeholder':'Enter password'}))
    captcha = CaptchaField()

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':25, 'rows': 10}))
    captcha = CaptchaField()
