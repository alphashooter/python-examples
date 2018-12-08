from django.http import HttpResponse
from .models import *


def add_author(request, first_name, last_name):
    Author.objects.create()