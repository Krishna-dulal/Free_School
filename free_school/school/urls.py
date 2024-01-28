from django.urls import path
from . import views

app_name = 'school'  # Replace 'myapp' with the actual app name

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_view, name="logout"),
]
