# Generated by Django 3.0.8 on 2020-08-16 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200816_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_type_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.RemoveField(
            model_name='projectapp',
            name='context',
        ),
        migrations.RemoveField(
            model_name='projectapp',
            name='value',
        ),
        migrations.RemoveField(
            model_name='projectcontent',
            name='order',
        ),
        migrations.AddField(
            model_name='projectclient',
            name='order',
            field=models.CharField(default=1, max_length=10),
        ),
        migrations.AddField(
            model_name='projectapp',
            name='app_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.AppType'),
        ),
    ]
