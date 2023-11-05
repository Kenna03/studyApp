from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_assignment/', views.create_assignment, name='create_assignment')
]
