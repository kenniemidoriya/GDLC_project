from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path("Students/", views.student_list, name="students"),
    path('/dashboard/', views.dashboard, name='dashboard'),
    path('/settings/', views.settings, name='settings'),
    
]
