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
    path('admin/users/', include('modules.admin.users.urls')),
    path('admin/courses/', include('modules.admin.courses.urls')),
    path('admin/schedules/', include('modules.admin.schedules.urls')),
    path('admin/notices/', include('modules.admin.notices.urls')),
    path('admin/dashboard/', include('modules.admin.dashboard.urls')),
    path('teacher/users/', include('modules.teacher.tch_users.urls')),
    path('teacher/courses/', include('modules.teacher.tch_courses.urls')),
    path('teacher/schedules/', include('modules.teacher.tch_schedules.urls')),
    path('teacher/notices/', include('modules.teacher.tch_notices.urls')),
    path('teacher/dashboard/', include('modules.teacher.tch_dashboard.urls')),
    path('student/users/', include('modules.student.std_users.urls')),
    path('student/courses/', include('modules.student.std_courses.urls')),
    path('student/schedules/', include('modules.student.std_schedules.urls')),
    path('student/notices/', include('modules.student.std_notices.urls')),
    path('student/dashboard/', include('modules.student.std_dashboard.urls')),
    # path('admin/', admin.site.urls),
]
