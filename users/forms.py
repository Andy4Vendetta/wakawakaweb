from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class RegisterForm(UserCreationForm):    
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 
                  'password1', 'password2', 'customer']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'patronymic', 
                  'phone_number', 'email', 'description']