from django.urls import path
from django.contrib.auth.views import (PasswordChangeView, 
                                       PasswordChangeDoneView, 
                                       LoginView, LogoutView)
                                       
from .views import RegisterView, ProfileView
from .forms import ChangePasswordForm


urlpatterns = [ 
    path('register', 
            RegisterView.as_view(), 
            name='register'),
    
    path('login', 
            LoginView.as_view(template_name='users/login.html',
                              redirect_authenticated_user=True),
            name='login'),
    
    path('password-change', 
            PasswordChangeView.as_view(
                    template_name='users/password_change.html',
                    form_class=ChangePasswordForm),
            name='password_change'),
    
    path('password-change-done', 
            PasswordChangeDoneView.as_view(
                    template_name='users/password_change_done.html'),
            name='password_change_done'),
    
    path('logout', 
            LogoutView.as_view(),  
            name='logout'),
    
    path('',
            ProfileView.as_view(),
            name='profile'),
]