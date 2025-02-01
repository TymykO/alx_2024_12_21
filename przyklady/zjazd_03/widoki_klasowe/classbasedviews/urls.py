"""classbasedviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView, ListView, DetailView
from examples.views import MyView, MyTemplateView, list_view, PersonListView
from examples.models import Person

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MyView.as_view()),
    path("template/", MyTemplateView.as_view()),
    path("template2/", TemplateView.as_view(template_name="template.html")),
    path("list/", list_view),
    path("list2/", ListView.as_view(model=Person)),
    path("list3/", PersonListView.as_view()),

    path("detail/<int:pk>/", DetailView.as_view(model=Person)),
]
