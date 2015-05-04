# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20150417_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating_star',
            field=models.FloatField(null=True),
            preserve_default=True,
        ),
    ]
