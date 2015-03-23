# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiscountInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('discount', models.CharField(max_length=200, verbose_name=b'\xe6\x8a\x98\xe6\x89\xa3')),
                ('url', models.URLField(verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5')),
                ('price', models.CharField(max_length=32, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('imgsrc', models.URLField(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80')),
                ('description', models.CharField(max_length=1000, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe4\xbf\xa1\xe6\x81\xaf')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f')),
                ('category', models.ForeignKey(to='discount.DiscountCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiscountWeb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('url', models.URLField(verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='discountinfo',
            name='source',
            field=models.ForeignKey(to='discount.DiscountWeb'),
            preserve_default=True,
        ),
    ]
