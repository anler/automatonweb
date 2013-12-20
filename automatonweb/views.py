# -*- coding: utf-8 -*-

from django import http
from django.template.response import TemplateResponse

from .st import regex_string_to_png


def home(request):
    return TemplateResponse(request, 'home.html')


def dot_graph(request):
    regex_string = request.REQUEST.get('regex')
    regex_string_to_png(regex_string)

    return http.HttpResponse()
