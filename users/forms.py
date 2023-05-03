from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.core.exceptions import ValidationError


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

    
class ResetPasswordForm(PasswordResetForm):
    def is_valid(self):
        email = self.data['email']
        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            user = None
        if not user:
            self.add_error('email', ValidationError('Нет пользователя с таким email'))
        return super().is_valid()