from django.db import models
from django.utils.translation import gettext as _
from datetime import date


class ProjectType(models.Model):
    name = models.CharField(max_length=45)
    label = models.CharField(max_length=45, default="")

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    path = models.CharField(max_length=45)
    alt = models.CharField(max_length=45, default="")
    vignette_path = models.CharField(max_length=45)
    vignette_alt = models.CharField(max_length=45, default="")


class AppType(models.Model):
    app_type_name = models.CharField(max_length=45)


class Project(models.Model):
    name = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    sub_title = models.CharField(max_length=45)
    active = models.SmallIntegerField(default=1)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, default=1)
    project_image = models.ForeignKey(ProjectImage, on_delete=models.CASCADE, default=1)
    created_at = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return self.name


class ProjectClient(models.Model):
    name = models.CharField(max_length=45)
    value = models.CharField(max_length=45)
    order = models.CharField(max_length=10, default=1)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectContent(models.Model):
    content = models.CharField(max_length=255)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectApp(models.Model):
    name = models.CharField(max_length=45)
    app_type_id = models.ForeignKey(AppType, on_delete=models.CASCADE, default=1)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectGalerie(models.Model):
    path = models.CharField(max_length=45)
    alt = models.CharField(max_length=45)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
