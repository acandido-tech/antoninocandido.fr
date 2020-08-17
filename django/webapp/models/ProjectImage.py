from django.db import models


class ProjectImage(models.Model):
    path = models.CharField(max_length=45)
    alt = models.CharField(max_length=45, default="")
    vignette_path = models.CharField(max_length=45)
    vignette_alt = models.CharField(max_length=45, default="")
