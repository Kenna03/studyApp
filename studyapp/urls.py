from django.urls import path
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('studyapp.views',
    url(r'^list/$', 'list', name='list'),
)
urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    path('create_assignment/', views.create_assignment, name='create_assignment'),
    path('collaboration/', views.collaboration, name='collaboration'),
]
