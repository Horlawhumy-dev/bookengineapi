# Generated by Django 3.2 on 2022-02-10 00:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_blockedday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedday',
            name='check_in',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 1, 40, 14, 235598)),
        ),
    ]
