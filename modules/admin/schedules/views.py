from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('admin/schedules/index.html')
    context = {"schedules_page": "active"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('admin/schedules/add.html')
    context = {"schedules_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('admin/schedules/edit.html')
    context = {"schedules_page_edit": "active"}
    return HttpResponse(template.render(context))


def delete(request):
    template = loader.get_template('admin/schedules/delete.html')
    context = {"schedules_page_delete": "active"}
    return HttpResponse(template.render(context))
