from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("SUBJECTS.")
# Create your views here.
