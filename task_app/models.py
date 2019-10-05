""" Task App Models """

from django.db import models
from django.urls import reverse

class Task(models.Model):
  """ Tasks to complete """
  task_title = models.CharField(max_length=200)
  task_description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  completed_at = models.DateTimeField(blank=True, null=True)

  def get_absolute_url(self):
    return reverse('task_app:task-create')
  
  def __str__(self):
    return self.task_title

