# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-09 23:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 1, 9, 23, 19, 44, 76454, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
