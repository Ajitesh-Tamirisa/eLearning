# Generated by Django 3.0.8 on 2020-07-31 07:21

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20200731_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.IntegerField(default=0, verbose_name=app.models.Course),
        ),
    ]