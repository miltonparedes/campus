from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('schedules/index.html')
    return HttpResponse(template.render())


def add(request):
    template = loader.get_template('schedules/add.html')
    return HttpResponse(template.render())


def edit(request):
    template = loader.get_template('schedules/edit.html')
    return HttpResponse(template.render())


def delete(request):
    template = loader.get_template('schedules/delete.html')
    return HttpResponse(template.render())
