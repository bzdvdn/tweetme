# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-06-12 09:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0006_auto_20180610_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]