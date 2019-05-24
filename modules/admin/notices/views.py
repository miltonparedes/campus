from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('admin/notices/index.html')
    context = {"notices_page": "active"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('admin/notices/add.html')
    context = {"notices_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('admin/notices/edit.html')
    return HttpResponse(template.render())


def delete(request):
    template = loader.get_template('admin/notices/delete.html')
    return HttpResponse(template.render())
