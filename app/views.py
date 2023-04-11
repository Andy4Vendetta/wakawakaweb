from django.shortcuts import render
from django.views.generic import (ListView, DetailView, FormView, 
                                  TemplateView, RedirectView)
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ServiceRequest, ServiceResponse
from .forms import ServiceRequestForm, ServiceResponseForm


class MainView(RedirectView):
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy('app:request_list')
        return reverse_lazy('app:info')


class InfoView(TemplateView):
    template_name = 'app/info.html'


class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'app/request_list.html'
    context_object_name = 'requests'
    
    
class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'app/request_detail.html'
    context_object_name = 'request'
    
    
class ServiceRequestCreateView(LoginRequiredMixin, FormView):
    model = ServiceRequest
    template_name = 'app/request_create.html'
    form_class = ServiceRequestForm
    success_url = reverse_lazy('app:main')
    
    def get_form(self, form_class=None):
            form = self.form_class(self.request.POST or None,
                                user=self.request.user)
            return form
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ServiceResponseListView(LoginRequiredMixin, ListView):
    model = ServiceResponse
    template_name = 'app/response_list.html'
    context_object_name = 'responses'


class ServiceResponseDetailView(LoginRequiredMixin, DetailView):
    model = ServiceResponse
    template_name = 'app/response_detail.html'
    context_object_name = 'response'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.watched = True
        obj.save()
        return obj
    
    


class ServiceResponseCreateView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = ServiceRequest
    template_name = 'app/response_create.html'
    form_class = ServiceResponseForm
    success_url = reverse_lazy('app:response_list')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = self.form_class(self.request.POST or None,
                               service_request=self.object,
                               user=self.request.user)
        return form
    
    
class NotificationsView(ListView):
    model = ServiceResponse
    template_name = 'app/notifications.html'
    context_object_name = 'responses'
    
    def get_queryset(self):
        queryset = self.model.objects.filter(
            service_request__customer=self.request.user,
            watched=False
        )
        return queryset