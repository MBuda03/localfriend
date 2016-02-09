# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20160209_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=100, decimal_places=2),
        ),
    ]
