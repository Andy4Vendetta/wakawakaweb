from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model
from django.urls import reverse_lazy

from .forms import RegisterForm


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('app:main')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('app:subject_list')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class ProfileView(LoginRequiredMixin, TemplateView):
   template_name = 'users/profile.html'
   
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['user'] = self.request.user
       return context