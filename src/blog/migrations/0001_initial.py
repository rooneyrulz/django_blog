# Generated by Django 2.2.5 on 2019-09-06 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 9, 7, 0, 45, 49, 298069))),
            ],
        ),
    ]
