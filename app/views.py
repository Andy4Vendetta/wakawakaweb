from django.views.generic import (ListView, DetailView, FormView, 
                                  TemplateView, RedirectView)
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .models import Category, ServiceRequest, ServiceResponse, Bookmark
from .forms import ServiceRequestForm, ServiceResponseForm, ServiceRequestSnippetFilter


class MainView(RedirectView):
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy('app:request_list')
        return reverse_lazy('app:info')


class InfoView(TemplateView):
    template_name = 'app/info.html'


class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'app/request_list.html'
    context_object_name = 'requests'
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(archived=False)
        if not self.kwargs.get('pk', None):
            return queryset
        return queryset.filter(category__id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = ServiceRequestSnippetFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'app/request_detail.html'
    context_object_name = 'request'


class ServiceRequestCreateView(LoginRequiredMixin, FormView):
    model = ServiceRequest
    template_name = 'app/request_create.html'
    form_class = ServiceRequestForm
    success_url = reverse_lazy('app:main')
    
    def get_form(self, form_class=None):
        form = self.form_class(self.request.POST or None,
                               self.request.FILES or None,
                                user=self.request.user)
        return form
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class ServiceResponseListView(LoginRequiredMixin, ListView):
    model = ServiceResponse
    template_name = 'app/response_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_customer:
            return queryset.filter(service_request__customer=self.request.user)
        return queryset.filter(user=self.request.user)
    

class ServiceResponseDetailView(LoginRequiredMixin, DetailView):
    model = ServiceResponse
    template_name = 'app/response_detail.html'
    context_object_name = 'response'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.watched = True
        obj.save()
        print(obj.watched)
        return obj
    
    
class ServiceResponseCreateView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = ServiceRequest
    template_name = 'app/response_create.html'
    form_class = ServiceResponseForm
    success_url = reverse_lazy('app:response_list')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = self.form_class(self.request.POST or None,
                               self.request.FILES or None,
                               service_request=self.object,
                               user=self.request.user)
        return form
    
    
class NotificationsView(LoginRequiredMixin, ListView):
    model = ServiceResponse
    template_name = 'app/notifications.html'
    context_object_name = 'responses'
    
    def get_queryset(self):
        queryset = self.model.objects.filter(
            service_request__customer=self.request.user
        )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responses_watched'] = context['responses'].filter(watched=True)
        context['responses'] = context['responses'].filter(watched=False)
        return context
    
class MyRequestsListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'app/my_requests_list.html'
    context_object_name = 'requests'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            customer=self.request.user
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requests'] = self.get_queryset().filter(archived=False)
        context['requests_archived'] = self.get_queryset().filter(archived=True)
        return context
        
    
class ServiceRequestEditView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = ServiceRequest
    template_name = 'app/my_requests_edit.html'
    form_class = ServiceRequestForm
    success_url = reverse_lazy('app:my_requests')
    context_object_name = 'request'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
            form = self.form_class(self.request.POST or None,
                                   self.request.FILES or None,
                                   instance=self.object)
            return form
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ServiceRequestDeleteView(LoginRequiredMixin, SingleObjectMixin, RedirectView):
    url = reverse_lazy('app:my_requests')
    model = ServiceRequest
    
    def get(self, request, *args, **kwargs,):
        obj = self.get_object()
        if not obj.customer == self.request.user:
            return redirect('app:main')
        obj.delete()
        return super().get(request, *args, **kwargs)
    

class ServiceRequestArchivedView(LoginRequiredMixin, SingleObjectMixin, RedirectView):
    url = reverse_lazy('app:my_requests')
    model = ServiceRequest
    
    def get(self, request, *args, **kwargs,):
        obj = self.get_object()
        if not obj.customer == self.request.user:
            return redirect('app:main')
        obj.archived = True
        obj.save()
        return super().get(request, *args, **kwargs)
    
    
class BookmarksListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'app/bookmark_list.html'
    context_object_name = 'requests'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(bookmarks__user=self.request.user)
    
    
class BookmarkCreateView(LoginRequiredMixin, SingleObjectMixin, RedirectView):
    model = ServiceRequest
    
    def get(self, request, *args, **kwargs,):
        service_request = self.get_object()
        user = self.request.user
        Bookmark.objects.create(
            service_request=service_request,
            user=user
        )
        return super().get(request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.META.get('HTTP_REFERER') or reverse_lazy('app:response_list')
        return url
    
    
class BookmarkDeleteView(LoginRequiredMixin, SingleObjectMixin, RedirectView):
    model = Bookmark
    
    def get(self, request, *args, **kwargs,):
        obj = self.get_object()
        if not obj.user == self.request.user:
            return redirect('app:main')
        obj.delete()
        return super().get(request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.META.get('HTTP_REFERER') or reverse_lazy('app:bookmarks')
        return url