# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150913_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(verbose_name=b'Article', blank=True, to='blog.Article'),
        ),
    ]
