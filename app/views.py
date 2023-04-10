from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy

from .models import ServiceRequest, ServiceResponse
from .forms import ServiceRequestForm, ServiceResponseForm


class ServiceRequestListView(ListView):
    model = ServiceRequest
    template_name = 'app/request_list.html'
    context_object_name = 'requests'
    
    
class ServiceRequestDetailView(DetailView):
    model = ServiceRequest
    template_name = 'app/request_detail.html'
    context_object_name = 'request'
    
class ServiceResponseCreateView(SingleObjectMixin, FormView):
    model = ServiceRequest
    template_name = 'app/response_create.html'
    form_class = ServiceResponseForm
    success_url = reverse_lazy('app:main')
    
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