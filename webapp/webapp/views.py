from django.http import HttpResponse
from .models import *


def add_author(request, first_name, last_name):
    obj = Author.objects.create(first_name=first_name, last_name=last_name)
    return HttpResponse('OK')


def get_authors(request):
    result = ['%s %s' % (author.first_name, author.last_name) for author in Author.objects.all()]
    return HttpResponse(', '.join(result))
