from django.urls import path
from django.contrib.auth.views import (PasswordChangeView, 
                                       PasswordChangeDoneView, 
                                       LoginView, LogoutView,)
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
                            
from .views import RegisterView, ProfileView, password_reset_request
from .forms import ChangePasswordForm


urlpatterns = [ 
    path('',
            ProfileView.as_view(),
            name='profile'),
    path('register/', 
            RegisterView.as_view(), 
            name='register'),
    path('login/', 
            LoginView.as_view(template_name='users/login.html',
                              redirect_authenticated_user=True),
            name='login'),
    path('logout/', 
            LogoutView.as_view(),  
            name='logout'),
    path('password-change/', 
            PasswordChangeView.as_view(
                    template_name='users/password_change.html',
                    form_class=ChangePasswordForm,
                    success_url=reverse_lazy('users:password_change_done')),
            name='password_change'),
    path('password-change-done/', 
            PasswordChangeDoneView.as_view(
                    template_name='users/password_change_done.html'),
            name='password_change_done'),
     path('password_reset/', 
          password_reset_request, 
          name="password_reset"),
     path('password_reset/done/', 
          auth_views.PasswordResetDoneView.as_view(
               template_name='users/password_reset_done.html'), 
          name='password_reset_done'),
     path('reset/<uidb64>/<token>/', 
          auth_views.PasswordResetConfirmView.as_view(
               template_name="users/password_reset_confirm.html",
               success_url = reverse_lazy('users:password_reset_complete')), 
          name='password_reset_confirm'),
     path('reset/done/', 
          auth_views.PasswordResetCompleteView.as_view(
               template_name='users/password_reset_complete.html'), 
          name='password_reset_complete'), 
]