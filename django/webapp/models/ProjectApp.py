from django.db import models
from .Project import Project
from .AppType import AppType


class ProjectApp(models.Model):
    name = models.CharField(max_length=45)
    app_type_id = models.ForeignKey(AppType, on_delete=models.CASCADE, default=1)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
