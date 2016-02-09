# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='price',
            field=models.DecimalField(default=b'0', max_digits=100, decimal_places=2),
        ),
    ]
