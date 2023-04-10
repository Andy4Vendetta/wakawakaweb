from django.views.generic import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from django.urls import reverse_lazy

from .forms import RegisterForm, ProfileForm


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