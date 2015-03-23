# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcategory',
            name='name',
            field=models.CharField(max_length=32, verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='discountweb',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90\xe7\xbd\x91\xe7\xab\x99'),
            preserve_default=True,
        ),
    ]
