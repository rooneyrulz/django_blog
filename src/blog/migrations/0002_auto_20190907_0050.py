# Generated by Django 2.2.5 on 2019-09-06 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 7, 0, 50, 32, 251361)),
        ),
    ]
