from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reset-password', views.reset_pass, name='reset_pass')
]
