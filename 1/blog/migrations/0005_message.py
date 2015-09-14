# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150912_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'content')),
                ('name', models.CharField(max_length=30, null=True, verbose_name=b'Name', blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
