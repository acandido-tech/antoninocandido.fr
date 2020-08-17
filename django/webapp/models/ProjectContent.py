from django.db import models
from .Project import Project


class ProjectContent(models.Model):
    content = models.CharField(max_length=255)
    color_setting = models.CharField(max_length=10, default="#c8c9ca")
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
