from django.urls import path
from . import views
from django.contrib import admin

app_name = 'school'  

urlpatterns = [
    path("", views.home, name="home"),
     path('<int:id>/', views.school, name='school'),
    path("logout/", views.logout_view, name="logout"),
]
