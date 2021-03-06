# Generated by Django 3.2 on 2022-02-10 00:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockedDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_price', models.IntegerField(blank=True, null=True)),
                ('check_in', models.DateField(default=datetime.datetime(2022, 2, 10, 1, 32, 56, 408746))),
                ('check_out', models.DateField(blank=True, null=True)),
                ('booking_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.bookinginfo')),
            ],
        ),
    ]
