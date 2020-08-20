from django.db import models


class ProjectType(models.Model):
    name = models.CharField(max_length=45)
    label = models.CharField(max_length=45, default="")

    def __str__(self):
        return self.name
