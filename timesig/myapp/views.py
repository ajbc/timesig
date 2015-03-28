# Create your views here.

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html', {'right_now':datetime.utcnow()})

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
    return render(request, 'profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })