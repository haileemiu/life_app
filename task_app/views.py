from django.shortcuts import render
from django.views.generic import edit
from django.views import generic

from task_app import models
from . import templates


# TODO: add login required

class TaskCreate(edit.CreateView):
  model = models.Task
  template_name = 'task_app/task_create.html'
  fields = ['task_title', 'task_description',]

class TaskList(generic.ListView):
  model = models.Task
  template_name = 'task_app/task_list.html'

class TaskDetail(generic.DetailView):
  model = models.Task
  template_name = 'task_app/task_detail.html'
  context_object_name = 'task'