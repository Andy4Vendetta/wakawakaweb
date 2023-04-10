from django import forms

from .models import ServiceRequest, ServiceResponse


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        
        
class ServiceResponseForm(forms.ModelForm):
    class Meta:
        model = ServiceResponse
        fields = '__all__'