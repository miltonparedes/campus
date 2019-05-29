from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('teacher/users/index.html')
    context = {"courses_page": "active"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('teacher/users/add.html')
    context = {"courses_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('teacher/users/edit.html')
    context = {"courses_page_edit": "active"}
    return HttpResponse(template.render(context))


def delete(request):
    template = loader.get_template('teacher/users/delete.html')
    context = {"courses_page_delete": "activate"}
    return HttpResponse(template.render(context))
