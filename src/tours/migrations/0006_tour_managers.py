# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tours', '0005_tour_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='managers',
            field=models.ManyToManyField(related_name='tour_manager', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
