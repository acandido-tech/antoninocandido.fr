from django.db import models
from . import Project


class ProjectClient(models.Model):
    name = models.CharField(max_length=45)
    value = models.CharField(max_length=45)
    order = models.CharField(max_length=10, default=1)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
