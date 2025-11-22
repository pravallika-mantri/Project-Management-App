from django.urls import path
from . import views

urlpatterns = [
    # Projects Urls
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create, name='project_create'),
    path('<int:pk>/edit/', views.project_update, name='project_update'),
    path('<int:pk>/delete/', views.project_delete, name='project_delete'),

    # Tasks Urls
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:project_pk>/tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('/tasks<int:pk>/delete/', views.task_delete, name='task_delete'),
]