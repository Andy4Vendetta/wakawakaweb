from django.urls import path

from .views import (ServiceRequestListView, ServiceRequestDetailView,
                    ServiceResponseCreateView)


urlpatterns = [
    path('', 
        ServiceRequestListView.as_view(), 
        name='main'),
    path('<int:pk>', 
        ServiceRequestDetailView.as_view(), 
        name='request_detail'),
    path('create/<int:pk>',
        ServiceResponseCreateView.as_view(), 
        name='response_create'),
]