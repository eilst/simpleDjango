# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from adress.models import Adress
from django.template import loader

# Create your views here.
def adress(request):
    adresss = Adress.objects.all()
    template = loader.get_template('adress/adress.html')
    context = {
        'adresss': adresss,
    }
    return HttpResponse(template.render(context,request))