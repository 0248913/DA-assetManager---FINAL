from dataclasses import fields
from turtle import textinput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserLog, Profile
from .models import Space
from django import forms
from .models import Group
from django.contrib.auth.forms import UserChangeForm
from .models import User
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm): 
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class UserLogForm(forms.ModelForm):
    last_changed_by = forms.CharField(required=False, label='Last Changed By')
    last_changed_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        required=False,
        label='Last Changed Date'
    )
    email = forms.EmailField(required=False, label='Email')


    return_by = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False,
        label='Return By'
    )

    class Meta:
        model = UserLog
        fields = ['title', 'information', 'in_use', 'last_changed_by', 'last_changed_date', 'return_by']


class CreateSpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name']
       
class SpaceCodeForm(forms.Form):
     code = forms.CharField(label='Join Code', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Join Code'}))

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members']   

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']