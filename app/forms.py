from django import forms

from .models import ServiceRequest, ServiceResponse


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        
        
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