# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20150427_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedback_time',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
