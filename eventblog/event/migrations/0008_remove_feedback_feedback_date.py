# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20150430_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='feedback_date',
        ),
    ]
