from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


class BooksView(ListView):
    template_name = 'app/main.html'
    model = Book
    context_object_name = 'books'