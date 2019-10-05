from django.shortcuts import render
from django.views.generic import edit
from django.views import generic

from task_app.models import Task
from . import templates


# TODO: add login required

class TaskCreate(edit.CreateView):
  model = Task
  template_name = 'task_app/task_create.html'
  fields = ['task_title', 'task_description',]

class TaskList(generic.ListView):
  model = Task
  template_name = 'task_app/task_list.html'

