"""
URL configuration for activity_enrollment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
# from django.urls import include, re_path
# from django.conf.urls import include
# from django.conf.urls import url

from sservice.views import *


# from sservice import urls as sservice_urls


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include(sservice_urls, namespace="sservice")),
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/volunteer/", Activity_View.as_view(), name="volunteer"),
    path("api/volunteer_enroll_unenroll/", Enroll_Unenroll_View.as_view(), name="enroll_unenroll")
]
