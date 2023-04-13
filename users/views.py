from django.views.generic import CreateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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
   

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = get_user_model().objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "users/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:80',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'wakawakaweb@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect('users:password_reset_done')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="users/password_reset.html", context={"password_reset_form":password_reset_form})