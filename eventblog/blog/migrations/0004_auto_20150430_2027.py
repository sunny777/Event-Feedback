# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150427_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_time',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
