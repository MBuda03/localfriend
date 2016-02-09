# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20160209_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
