from .models import User, ProfileUser, Posting
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

class Register(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'})
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'})
    )
    password2 = None # Menghilangkan konfirmasi password
    
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password confirmation'})
    # )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1')

class Login(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ('image',)

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('content',)

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','phone','address')