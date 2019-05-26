from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.index, name='add'),
    path('edit', views.index, name='edit'),
    path('delete', views.index, name='delete')
]
