from django.db import models


class AppType(models.Model):
    app_type_name = models.CharField(max_length=45)
