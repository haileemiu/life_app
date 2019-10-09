from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView, UpdateView
from django.urls import reverse

from task_app import models
from . import templates


# TODO: add login required

class TaskCreate(CreateView):
  model = models.Task
  template_name = 'task_app/task_create.html'
  fields = ['task_title', 'task_description',]

class TaskList(ListView):
  model = models.Task
  template_name = 'task_app/task_list.html'

class TaskDetail(DetailView):
  model = models.Task
  template_name = 'task_app/task_detail.html'
  context_object_name = 'task'

class TaskEdit(UpdateView):
  model = models.Task
  fields = ['task_title', 'task_description']
  form = 'task_app/task_form.html'
