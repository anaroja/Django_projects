# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    random_world = get_random_string(length=14)
    details = {
        'generated': random_world,
    }
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1

    return render(request, 'randomworld/index.html', details) 


def reset(request):
    del request.session['counter']
    return redirect('/')