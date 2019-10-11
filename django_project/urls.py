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
    
    # student
    path('home', homepage),
    path('my_request/', my_request),
    path('request/', requestt),
    
    # librarian
    path('lib_home', lib_homepage),
    path('book_bank', bookbank),
    path('select_bbank/<str:val>', select_bbank),
    path('issue/<str:val>', issue),
    path('return/<str:val>', book_bank_return),
    path('pending_request', pending_request),
    path('view_request/<int:id>', view_request),
    path('image_view/<str:id>', image_view),
    path('decide/<str:id>', decide),
    path('deduct/<str:id>', deduct),
    path('report', generate_report),

    # accountant
    path('acc_home', acc_homepage),
    path('report_accountant', generate_report_accountant),
    path('pending_request_accountant', pending_request_accountant),
    path('view_request_accountant/<int:id>', view_request_accountant),
    path('decide_acc/<str:id>', decide_acc),

    # for all
    path('', login),
    path('login/<str:desig>', user_login),
    path('logout/<str:desig>', logout),
    path('otplogin/<str:desig>', otp_login),
    path('change_password/<str:desig>', change_pass),
    path('set_pass/<str:desig>', set_pass),
    path('getotp/<str:desig>', get_otp),

    # others
    path('clean', clean),
    path('delete/<int:identity>', delete_emp),
    path('update/<int:identity>', update_emp),
    path('add', add_emp),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
