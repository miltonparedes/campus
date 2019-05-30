from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('admin/users/index.html')
    context = {"users_page": "active"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('admin/users/add.html')
    context = {"users_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('admin/users/edit.html')
    context = {"users_page_edit": "active"}
    return HttpResponse(template.render(context))
