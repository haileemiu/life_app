from django.urls import path

from . import views

app_name = 'task_app'

urlpatterns = [
    path('create/', views.TaskCreate.as_view(), name='task-create'),
]