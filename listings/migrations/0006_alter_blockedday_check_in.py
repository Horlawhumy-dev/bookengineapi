# Generated by Django 3.2 on 2022-02-10 01:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_blockedday_check_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockedday',
            name='check_in',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
