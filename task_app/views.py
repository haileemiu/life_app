from django.shortcuts import render
from django.views.generic.edit import CreateView

from task_app.models import Task
from . import templates


# TODO: add login required

class TaskCreate(CreateView):
  model = Task
  template_name = 'task_app/task_create.html'
  fields = ['task_title', 'task_description',]
