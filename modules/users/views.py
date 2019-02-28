from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('users/index.html')
    return HttpResponse(template.render())


def add(request):
    template = loader.get_template('users/add.html')
    return HttpResponse(template.render())


def edit(request):
    template = loader.get_template('users/edit.html')
    return HttpResponse(template.render())


def delete(request):
    template = loader.get_template('users/delete.html')
    return HttpResponse(template.render())
