# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150911_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='imageURL',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
