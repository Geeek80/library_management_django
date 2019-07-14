"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from .views import *
from django_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contactpg),
    path('about/', aboutpg),
    path('', homepage),
    path('add', add_emp),
    path('show/', show_emp),
    path('edit/<int:id>', edit_emp),
    path('update/<int:identity>', update_emp),
    path('delete/<int:identity>', delete_emp),
    path('login/<str:desig>', user_login),
    path('my_request/', my_request),
    path('request/', requestt),
    path('logout/<str:desig>', logout),
    path('upload_csv', upload_csv),
    path('otplogin/<str:desig>', otp_login),
    path('pending_request', pending_request),
    # path('clean', clean),
]
