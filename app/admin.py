from django.contrib import admin

from .models import Category, ServiceRequest, ServiceResponse

admin.site.register(Category)
admin.site.register(ServiceRequest)
admin.site.register(ServiceResponse)