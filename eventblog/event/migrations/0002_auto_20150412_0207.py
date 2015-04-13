# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating_star',
            field=models.IntegerField(choices=[(b' 1 ', b'One'), (b' 2 ', b'Two'), (b' 3 ', b'Three'), (b' 4 ', b'Four'), (b' 5 ', b'Five')]),
            preserve_default=True,
        ),
    ]
