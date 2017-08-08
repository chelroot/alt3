#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404


# Create your views here.
# def login(request):
#     pass


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")



def login(request):
    if request.method == 'POST':
        print("POST data =", request.POST)
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, 'index.html', {'username': username, 'errors': True})
    raise Http404