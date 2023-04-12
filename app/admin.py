from django.contrib import admin

from .models import Category, ServiceRequest, ServiceResponse, Bookmark

admin.site.register(Category)
admin.site.register(Bookmark)
admin.site.register(ServiceRequest)
admin.site.register(ServiceResponse)