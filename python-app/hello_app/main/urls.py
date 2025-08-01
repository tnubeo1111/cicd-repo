from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('devops_tools/', views.devops_tools, name='devops_tools'),
]