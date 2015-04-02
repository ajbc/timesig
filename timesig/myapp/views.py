# Create your views here.

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import Context
from timesig.myapp.models import *

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

def docs(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)

    myDocs = UserDoc.objects.filter(user=request.user.id).filter(active=True).order_by('-lastModified')
    docs = Doc.objects.all()
    userDocs = []
    candidateDocs = []

    userDocIds = set()
    for ud in myDocs:
        userDocs.append(Doc.objects.get(pk=ud.doc))
        userDocIds.add(ud.doc)

    for doc in docs:
        if doc.id not in userDocIds:
            candidateDocs.append(doc)

    context = Context({'userDocs': userDocs, 'candidateDocs': candidateDocs})

    return render(request, 'docs.html', context)

def doc(request, doc_id):
    try:
        myDoc = UserDoc.objects.filter(user=request.user.id).filter(doc=doc_id)[0]
    except IndexError:
        myDoc = UserDoc.objects.create(user=request.user.id, doc=doc_id, \
            active=False, lastModified=datetime.utcnow(), lastLocation=0)
    return doc_loc(request, doc_id, myDoc.lastLocation)

def doc_loc(request, doc_id, loc):
    # yellow, aqua, fushia, grey
    #nav = [prev_my_anchor, prev_anchor, prev_possible, prev, next, next_possible, next_anchor, next_my_anchor]
    nav = [0, 1, 2, 3, 4, 5]
    words = "<p>example</p>"
    return render(request, 'doc.html', {'doc': Doc.objects.get(pk=doc_id), 'words': words, 'nav': nav})