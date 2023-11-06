from django.urls import path
# noinspection PyUnresolvedReferences
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    path('create_assignment/', views.create_assignment, name='create_assignment'),
    path('collaboration/', views.collaboration, name='collaboration'),
]
