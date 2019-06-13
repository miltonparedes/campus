from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('teacher/schedules/index.html')
    context = {"schedules_page": "active"}
    return HttpResponse(template.render(context))
