from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('teacher/courses/index.html')
    context = {"courses_page": "open"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('teacher/courses/add.html')
    context = {"courses_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('teacher/courses/edit.html')
    context = {"courses_page_edit": "active"}
    return HttpResponse(template.render(context))


def delete(request):
    template = loader.get_template('teacher/courses/delete.html')
    context = {"courses_page_delete": "activate"}
    return HttpResponse(template.render(context))
