from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def index(request):
    template = loader.get_template('dashboard/index.html')
    context = {"dashboard_page": "active"}
    return HttpResponse(template.render(context))
