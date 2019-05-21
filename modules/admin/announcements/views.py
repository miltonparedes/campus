from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('admin/announcements/index.html')
    context = {"announcements_page": "active"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('admin/announcements/add.html')
    context = {"announcements_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('admin/announcements/edit.html')
    return HttpResponse(template.render())


def delete(request):
    template = loader.get_template('admin/announcements/delete.html')
    return HttpResponse(template.render())
