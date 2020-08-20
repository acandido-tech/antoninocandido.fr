from django.db import models
from django.utils.translation import gettext as _
from datetime import date
from .ProjectType import ProjectType
from .ProjectImage import ProjectImage


class Project(models.Model):
    name = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    sub_title = models.CharField(max_length=45)
    active = models.SmallIntegerField(default=1)
    project_type = models.ForeignKey(
        ProjectType, on_delete=models.CASCADE, default=1
    )
    project_image = models.ForeignKey(
        ProjectImage, on_delete=models.CASCADE, default=1
    )
    created_at = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return self.name
