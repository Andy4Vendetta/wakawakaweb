from django.contrib import admin

from .models import ServiceRequest, ServiceResponse


admin.site.register(ServiceRequest)
admin.site.register(ServiceResponse)