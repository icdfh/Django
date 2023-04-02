from django import forms
from django.core.exceptions import ValidationError


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
            username = forms.CharField(label='Login',widget=forms.TextInput(attrs={'class':'form-input'}))
            username = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class:''form-input'}))
            username = forms.CharField(label='Confrim Password', widget=forms.PasswordInput(attrs={'class':'form-input'}))
            class Meta:
                model = User
                fields = ('username' , 'password1', 'password2')
                widgets = {
                    'username': forms.TextInput(attrs={'class':'form-input'}),
                    'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
                    'password2': forms.PasswordInput(attrs={'class':'form-input'}),
                }
