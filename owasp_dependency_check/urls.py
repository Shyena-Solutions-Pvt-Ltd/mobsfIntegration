from django.urls import path
from . import views
from .views import run_dependency_check



urlpatterns = [
    path('', views.run_dependency_check, name='run_dependency_check'),
    path('run-dependency-check/', run_dependency_check, name='run_dependency_check'),
]
