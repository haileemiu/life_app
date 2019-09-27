""" Task App Models """

from django.db import models

class Task(models.Model):
  """ Tasks to complete """
  task_title = models.CharField(max_length=200)
  task_description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  completed_at = models.DateTimeField(blank=True)
