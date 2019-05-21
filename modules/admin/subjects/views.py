from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('admin/subjects/index.html')
    context = {"subjects_page": "active"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('admin/subjects/add.html')
    context = {"subjects_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('admin/subjects/edit.html')
    context = {"subjects_page_edit": "active"}
    return HttpResponse(template.render(context))


def delete(request):
    template = loader.get_template('admin/subjects/delete.html')
    context = {"subjects_page_delete": "activate"}
    return HttpResponse(template.render(context))
