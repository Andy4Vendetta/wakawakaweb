from django.contrib import admin

from .models import Category, ServiceRequest, ServiceResponse, Bookmark


admin.site.register(Category)
admin.site.register(ServiceRequest)
admin.site.register(ServiceResponse)
admin.site.register(Bookmark)