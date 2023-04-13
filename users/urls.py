from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import (PasswordChangeView, 
                                       PasswordChangeDoneView, 
                                       LoginView, LogoutView,)
                            
from .views import RegisterView, ProfileView, PasswordResetRequestView


urlpatterns = [ 
    path('',
            ProfileView.as_view(),
            name='profile'),
    path('register/', 
            RegisterView.as_view(), 
            name='register'),
    path('login/', 
            LoginView.as_view(
                template_name='users/login.html',
                redirect_authenticated_user=True),
            name='login'),
    path('logout/', 
            LogoutView.as_view(),  
            name='logout'),
    path('password_change/', 
            PasswordChangeView.as_view(
                template_name='users/password_change.html',
                form_class=PasswordChangeForm,
                success_url=reverse_lazy('users:password_change_done')),
            name='password_change'),
    path('password_change_done/', 
            PasswordChangeDoneView.as_view(
                template_name='users/password_change_done.html'),
            name='password_change_done'),
     path('password_reset/', 
            PasswordResetRequestView.as_view(), 
          name="password_reset"),
     path('password_reset/done/', 
          auth_views.PasswordResetDoneView.as_view(
               template_name='users/password_reset_done.html'), 
          name='password_reset_done'),
     path('reset/<uidb64>/<token>/', 
          auth_views.PasswordResetConfirmView.as_view(
               template_name="users/password_reset_confirm.html",
               success_url=reverse_lazy('users:password_reset_complete'),
               post_reset_login=True), 
          name='password_reset_confirm'),
     path('reset/complete/', 
          auth_views.PasswordResetCompleteView.as_view(
               template_name='users/password_reset_complete.html'), 
          name='password_reset_complete'), 
]