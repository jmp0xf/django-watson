# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchentry',
            name='lang',
            field=models.CharField(default='', max_length=10, blank=True),
        ),
    ]
