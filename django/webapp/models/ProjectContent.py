from django.db import models
from .Project import Project


class ProjectContent(models.Model):
    content = models.CharField(max_length=255)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
