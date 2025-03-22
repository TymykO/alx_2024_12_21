from django.urls import path
from . import views


urlpatterns = [
     path("examples/sync/", views.sync_example, name="sync-example"),
     path("examples/async/", views.async_example, name="async-example"),

]
