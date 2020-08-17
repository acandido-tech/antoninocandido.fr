from django.db import models
from .Project import Project


class ProjectGalerie(models.Model):
    path = models.CharField(max_length=45)
    alt = models.CharField(max_length=45)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
