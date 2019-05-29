from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('student/dashboard/index.html')
    context = {"dashboard_page": "active"}
    return HttpResponse(template.render(context))
