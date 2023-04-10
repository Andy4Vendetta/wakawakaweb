from django.urls import path

from .views import ServiceRequestListView, ServiceRequestDetailView


urlpatterns = [
    path('', ServiceRequestListView.as_view(), name='main'),
    path('<int:pk>', ServiceRequestDetailView.as_view(), name='request_detail')
]