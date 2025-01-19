from django.urls import path
from django.urls import reverse_lazy
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('', views.home, name='home'),
] 