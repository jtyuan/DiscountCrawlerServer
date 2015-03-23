# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '__first__'),
        ('discount', '0002_auto_20150323_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountinfo',
            name='checker_runtime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discountweb',
            name='scraper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.Scraper', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discountweb',
            name='scraper_runtime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True),
            preserve_default=True,
        ),
    ]
