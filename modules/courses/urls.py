from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('classroom', views.classroom, name='classroom'),
    path('add_classroom', views.add_classroom, name='add_classroom'),
    path('edit_classroom', views.edit_classroom, name='edit_classroom'),
    path('categoty', views.category, name='category'),
    path('add_category', views.add_category, name='add_category'),
    path('edit_category', views.edit_category, name='edit_category'),
]
