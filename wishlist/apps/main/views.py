# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from models import *
from time import localtime, strftime

# Create your views here.
def index(request):   
    return redirect('/main')

def main(request):
    return render(request, 'main/index.html')

def register(request):
    print request.POST
    result = User.objects.validate_reg(request.POST)
    if result[0]:
        # if true we register
        request.session['user_id'] = result[1].id
        request.session['user_name'] = result[1].name
        return redirect('/')
    else:
        # show errors
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)

        return redirect('/')

def login(request):
    if request.method == 'POST':
        result = User.objects.validate_log(request.POST)
        if result[0]:
            # we login
            request.session['user_id'] = result[1].id
            request.session['user_name'] = result[1].name
            return redirect('/success')
        else:
            # show errors
            for error in result[1]:
                messages.add_message(request, messages.INFO, error)

            return redirect('/')

    return redirect('/')        


def success(request):
    return render(request, 'main/logged.html')

def clear(request):
    request.session.clear()
    return redirect('/')     
