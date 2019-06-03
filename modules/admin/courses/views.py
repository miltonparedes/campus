from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('admin/courses/index.html')
    context = {"courses_page": "active"}
    return HttpResponse(template.render(context))


def add(request):
    template = loader.get_template('admin/courses/add.html')
    context = {"courses_page_add": "active"}
    return HttpResponse(template.render(context))


def edit(request):
    template = loader.get_template('admin/courses/edit.html')
    context = {"courses_page_edit": "active"}
    return HttpResponse(template.render(context))


def delete(request):
    template = loader.get_template('admin/courses/delete.html')
    context = {"courses_page_delete": "active"}
    return HttpResponse(template.render(context))

def classroom(request):
    template = loader.get_template('admin/courses/classroom.html')
    context = {"classroom_page_classroom": "active"}
    return HttpResponse(template.render(context))

def add_classroom(request):
    templalte = loader.get_tempalte('admin/courses/add_classroom.html')
    context = {"couses_page_add_classroom": "active"}
    return HttpResponse(template.render(context))

def edit_classroom(request):
    template = loader.get_template('admin/courses/edit_classroom.html')
    context = {"courses_page_edit_classroom": "active"}
    return HttpResponse(template.render(context))

def category(request):
    template = loader.get_template('admin/courses/category.html')
    context = {"courses_page_category": "active"}
    return HttpResponse(template.render(context))

def add_category(request):
    template = loader.get_template('admin/courses/add_category.html')
    context = {"courses_page_add_category": "active"}
    return HttpResponse(template.render(context))

def edit_category(request):
    template = loader.get_template('admin/courses/edit_category.html')
    context = {"couses_page_edit_category": "active"}
    return HttpResponse(template.render(context))
