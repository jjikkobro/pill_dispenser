"""
URL configuration for pill_dispenser project.

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
from django.views.generic.base import TemplateView
from notes.views import note_list_view,finish_item,delete_item,recover_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path("registration/", include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('profile/', TemplateView.as_view(template_name="home/profile.html"), name="profile"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('note/', note_list_view,name='note-list'),
    path('note/finish-item/<id>/', finish_item,name='finish-note-item'),
    path('note/recover-item/<id>/', recover_item,name='recover-note-item'),
    path('note/delete-item/<id>/', delete_item,name='delete-note-item')
]
