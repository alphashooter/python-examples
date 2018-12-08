from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    books = models.ManyToManyField(Book)
