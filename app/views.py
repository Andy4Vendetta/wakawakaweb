from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ServiceRequest


class ServiceRequestListView(ListView):
    model = ServiceRequest
    template_name = 'app/service_request_list.html'
    context_object_name = 'requests'
    
    
class ServiceRequestDetailView(DetailView):
    model = ServiceRequest
    template_name = 'app/service_request_detail.html'
    context_object_name = 'request'