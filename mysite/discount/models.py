# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy.contrib.djangoitem import DjangoItem


class DiscountWeb(models.Model):
    name = models.CharField('来源网站', max_length=200)
    url = models.URLField('链接', max_length=200)
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class DiscountCategory(models.Model):
    name = models.CharField('类别', max_length=32)

    def __unicode__(self):
        return self.name


class DiscountInfo(models.Model):
    category = models.ForeignKey(DiscountCategory)
    name = models.CharField('标题', max_length=200)
    discount = models.CharField('折扣', max_length=200)
    url = models.URLField('链接', max_length=200)
    price = models.CharField('价格', max_length=32)
    imgsrc = models.URLField('图片地址', max_length=200)
    description = models.CharField('详细信息', max_length=1000)
    date = models.DateTimeField('添加日期', auto_now_add=True)
    source = models.ForeignKey(DiscountWeb)
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name + ':' + self.price

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布？'


class DiscountItem(DjangoItem):
    django_model = DiscountInfo

@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, DiscountWeb):
        if instance.scraper_runtime:
            instance.scraper_runtime.delete()

    if isinstance(instance, DiscountInfo):
        if instance.checker_runtime:
            instance.checker_runtime.delete()

pre_delete.connect(pre_delete_handler)