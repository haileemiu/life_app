from django.urls import path

from . import views

app_name = 'task_app'

urlpatterns = [
    path('create/', views.TaskCreate.as_view(), name='task-create'),
    path('list/', views.TaskList.as_view(), name='task-list'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('edit/<int:pk>/', views.TaskEdit.as_view(), name='task-edit'),
]