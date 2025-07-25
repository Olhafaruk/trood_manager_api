# Generated by Django 5.2.4 on 2025-07-06 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='deadline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=10),
            preserve_default=False,
        ),
    ]
