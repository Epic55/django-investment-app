from django import forms
from .models import ModelClass, Employee, GeeksModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Your username',
      'class': 'w-full py-4 px-6 rounded-xl'
   }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
      'placeholder': 'Your password',
      'class': 'w-full py-4 px-6 rounded-xl'
   }))

class SignupForm(UserCreationForm):
   class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')

   username = forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Your username',
      'class': 'w-full py-4 px-6 rounded-xl'
   }))
   email = forms.CharField(widget=forms.EmailInput(attrs={
      'placeholder': 'Your email address',
      'class': 'w-full py-4 px-6 rounded-xl'
   }))
   password1 = forms.CharField(widget=forms.PasswordInput(attrs={
      'placeholder': 'Your password',
      'class': 'w-full py-4 px-6 rounded-xl'
   }))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={
      'placeholder': 'Repeat password',
      'class': 'w-full py-4 px-6 rounded-xl'
   }))

class GeeksForm(forms.ModelForm):
   class Meta:
      model = GeeksModel
      fields = [
         "title",
         "description",
      ]

#CLASS BASED VIEW
class EmployeeForm(forms.ModelForm):
   class Meta:
      model = Employee
      fields = '__all__'

class FormClass(forms.Form):
   title = forms.CharField()
   description = forms.CharField()
   price = forms.IntegerField()

class ModelFormClass(forms.ModelForm):
   class Meta:
      model = ModelClass
      fields = "__all__"