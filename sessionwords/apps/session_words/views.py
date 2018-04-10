# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from time import localtime, strftime
# Create your views here.
def index(request):
    if 'word' not in request.session:
        request.session['word'] = []
    context = {
    "time": strftime("%a, %d %b %Y %H:%M %p", localtime())
    }    
    return render(request, 'session_words/index.html', context)

def add_word(request):
    if request.method == 'POST': 
        request.session['word'].append(request.POST)
        request.session.modified = True
        return redirect('/')


def clear(request):
    if request.method == 'POST':
        del request.session['word']
        return redirect('/')        