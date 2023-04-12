from django import forms
from django.core.exceptions import ValidationError
from django_filters import FilterSet

from .models import Category, ServiceRequest, ServiceResponse


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        widgets = {
            'customer':forms.HiddenInput(),
            'archived':forms.HiddenInput(),
        }
        
    def __init__(self, data, files, user=None, *args, **kwargs):
        super(ServiceRequestForm, self).__init__(data, files, *args, **kwargs)
        self.fields['customer'].initial = user
        self.fields['archived'].initial = False


class ServiceResponseForm(forms.ModelForm):
    class Meta:
        model = ServiceResponse
        fields = '__all__'
        widgets = {
            'service_request':forms.HiddenInput(),
            'user':forms.HiddenInput(),
            'watched':forms.HiddenInput(),
        }
    def __init__(self, data, files, service_request=None, user=None, *args, **kwargs):
        super(ServiceResponseForm, self).__init__(data, files, *args, **kwargs)
        self.fields['service_request'].initial = service_request
        self.fields['user'].initial = user
        self.fields['watched'].initial = False
        
        
class ServiceRequestSnippetFilter(FilterSet):
    class Meta:
        model = ServiceRequest
        fields = {'title': ['icontains']}