from django.shortcuts import redirect
from django.views.generic import CreateView, FormView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings

from .forms import RegisterForm, ProfileForm, ResetPasswordForm


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('app:main')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app:main')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class ProfileView(LoginRequiredMixin, FormView):
   template_name = 'users/profile.html'
   form_class = ProfileForm
   success_url = reverse_lazy('users:profile')
   
   def get_form(self, form_class=None):
       form = self.form_class(self.request.POST or None,
           instance=self.request.user)
       return form

   def form_valid(self, form):
       form.save()
       return super().form_valid(form)


class PasswordResetRequestView(FormView):
    template_name = "users/password_reset.html"
    form_class = ResetPasswordForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password_reset_form'] = context.pop('form')
        return context

    def form_valid(self, form):
        subject = "Запрошен сброс пароля"
        email_template_name = "users/password_reset_email.txt"
        email=form.cleaned_data['email']
        user = get_user_model().objects.get(email=email)
        tags = {
        "email":user.email,
        'domain':settings.ALLOWED_HOSTS[0],
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "user": user,
        'token': default_token_generator.make_token(user),
        'protocol': 'http',
        }
        message = render_to_string(email_template_name, tags)
        try:
            send_mail(subject=subject, 
                      message=message, 
                      from_email='wakawakaweb@gmail.com',
                      recipient_list=[user.email],
                      fail_silently=False,
                      )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('users:password_reset_done')