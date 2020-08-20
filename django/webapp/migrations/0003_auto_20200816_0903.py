# Generated by Django 3.0.8 on 2020-08-16 07:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0002_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.CharField(max_length=45)),
                ("alt", models.CharField(max_length=45)),
                ("vignette_path", models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="created_at",
            field=models.DateField(default=datetime.date.today, verbose_name="Date"),
        ),
        migrations.AddField(
            model_name="project",
            name="project_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="webapp.ProjectType",
            ),
        ),
        migrations.CreateModel(
            name="ProjectGalerie",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.CharField(max_length=45)),
                ("alt", models.CharField(max_length=45)),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="webapp.Project"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectContent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=255)),
                ("order", models.CharField(max_length=10)),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="webapp.Project"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectClient",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=45)),
                ("value", models.CharField(max_length=45)),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="webapp.Project"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectApp",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=45)),
                ("value", models.CharField(max_length=45)),
                ("context", models.CharField(max_length=10)),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="webapp.Project"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="project_image",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="webapp.ProjectImage",
            ),
        ),
    ]
