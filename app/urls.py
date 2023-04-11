from django.urls import path

from .views import (ServiceRequestListView, ServiceRequestDetailView, ServiceRequestCreateView,
                    ServiceResponseListView, ServiceResponseDetailView, ServiceResponseCreateView,
                    InfoView, MainView, NotificationsView)


urlpatterns = [
     path('', 
          MainView.as_view(),
          name='main'),
     path('info/', 
          InfoView.as_view(),
          name='info'),
     path('notifications/',
          NotificationsView.as_view(),
          name='notifications'),
     path('requests/', 
          ServiceRequestListView.as_view(), 
          name='request_list'),
     path('requests/<int:pk>/', 
          ServiceRequestDetailView.as_view(), 
          name='request_detail'),
     path('requests/create/', 
          ServiceRequestCreateView.as_view(), 
          name='request_create'),
     path('responses/',
          ServiceResponseListView.as_view(),
          name='response_list'),
     path('responses/<int:pk>/',
         ServiceResponseDetailView.as_view(),
         name='response_detail'),
     path('responses/create/<int:pk>/',
         ServiceResponseCreateView.as_view(), 
         name='response_create'),
]