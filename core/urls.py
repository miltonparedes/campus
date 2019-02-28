"""campus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('modules.login.urls')),
    path('users/', include('modules.users.urls')),
    path('subjects/', include('modules.subjects.urls')),
    path('schedules/', include('modules.schedules.urls')),
    path('payments/', include('modules.payments.urls')),
    path('announcements/', include('modules.announcements.urls')),
    path('admin/', admin.site.urls),
]
