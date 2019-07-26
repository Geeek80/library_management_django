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

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('add', add_emp),
    path('all_requests/', all_requests),
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
    path('view_request/<int:id>', view_request),
    path('change_password/<str:desig>', change_pass),
    path('set_pass/<str:desig>', set_pass),
    path('getotp/<str:desig>', get_otp),
    path('image_view/<str:id>', image_view),
    path('decide/<str:id>', decide),
    path('deduct/<str:id>', deduct),
    path('report', generate_report),
    path('clean', clean),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
