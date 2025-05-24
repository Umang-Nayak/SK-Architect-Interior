"""
URL configuration for sk_interior project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from engine_app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', index_page, name="home"),
    path('about-us/', about_us_page, name="about"),
    path('project/', project_page, name="project"),
    path('contact/', contact_page, name="contact"),
    path('service/', service_page, name="service"),
    path('create_user_feedback/', submit_user_feedback, name="create_user_feedback"),
    path('create_contact_details/', submit_user_contact_details, name="create_contact_details"),
    path('project_information/<int:id>', project_detail_page, name="project_information"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
