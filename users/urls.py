from django.urls import path
from django.contrib.auth.views import (PasswordChangeView, 
                                       PasswordChangeDoneView, 
                                       LoginView, LogoutView)
from django.urls import reverse_lazy
                            
from .views import RegisterView, ProfileView
from .forms import ChangePasswordForm


urlpatterns = [ 
    path('',
            ProfileView.as_view(),
            name='profile'),
    path('register', 
            RegisterView.as_view(), 
            name='register'),
    path('login', 
            LoginView.as_view(template_name='users/login.html',
                              redirect_authenticated_user=True),
            name='login'),
    path('logout', 
            LogoutView.as_view(),  
            name='logout'),
    path('password-change', 
            PasswordChangeView.as_view(
                    template_name='users/password_change.html',
                    form_class=ChangePasswordForm,
                    success_url=reverse_lazy('users:password_change_done')),
            name='password_change'),
    path('password-change-done', 
            PasswordChangeDoneView.as_view(
                    template_name='users/password_change_done.html'),
            name='password_change_done'),
]