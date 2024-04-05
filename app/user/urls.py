"""Url mappings for user API"""
from django.urls import path
from user import views

app_name = 'user'   #used for reverse mapping
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),

]