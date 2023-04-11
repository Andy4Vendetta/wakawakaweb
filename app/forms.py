from django import forms

from .models import ServiceRequest, ServiceResponse


class ServiceRequestForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price_from = forms.DecimalField(min_value=0)
    price_to = forms.DecimalField(min_value=0)
    place = forms.CharField(widget=forms.Textarea)
    term = forms.DecimalField(min_value=0)
        
    def __init__(self, data, user, *args, **kwargs):
        super(ServiceRequestForm, self).__init__(data, *args, **kwargs)
        self.customer = user
    
    def save(self, commit=True):
        return ServiceRequest.objects.create(
            **self.cleaned_data,
            customer=self.customer,
        )
    
class ServiceResponseForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    def __init__(self, data, service_request, user, *args, **kwargs):
        super(ServiceResponseForm, self).__init__(data, *args, **kwargs)
        self.service_request = service_request
        self.user = user
        
    
    def save(self, commit=True):
        return ServiceResponse.objects.create(
            service_request = self.service_request,
            user = self.user,
            text = self.cleaned_data['text'],
            watched=False
        )