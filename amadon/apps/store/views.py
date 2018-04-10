# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def amadon(request):
    if 'total' not in request.session:
        request.session['total'] = 0
        request.session['items'] = 0


    return render(request, 'store/index.html')

def order(request):
    if request.method == 'POST':
        temp = request.POST
        total = float(temp['price'])*float(temp['quantity'])
        request.session['charged'] = total
        request.session['total'] += total
        request.session['items'] +=int(temp['quantity'])
        
    request.session.modified = True
    return redirect('/amadon/checkout')  

def checkout(request):
    return render(request, 'store/checkout.html')

def clear(request):
        request.session.clear()
        return redirect('/amadon')