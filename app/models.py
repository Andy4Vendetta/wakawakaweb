from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books')