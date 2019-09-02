from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = loader.get_template('users/index.html')
    context = {"users_page": "active"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('users/add.html')
    context = {"users_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('users/edit.html')
    context = {"users_page_edit": "active"}
    return HttpResponse(template.render(context))
