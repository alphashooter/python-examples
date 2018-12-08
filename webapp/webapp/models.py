from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    books = models.ManyToManyField(Book)
