# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'comment')),
                ('username', models.CharField(max_length=30, null=True, verbose_name=b'Name', blank=True)),
                ('email', models.EmailField(max_length=50, null=True, verbose_name=b'Email', blank=True)),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'PublishTime')),
                ('article', models.ForeignKey(verbose_name=b'Article', blank=True, to='blog.Article', null=True)),
                ('pid', models.ForeignKey(verbose_name=b'PComment', blank=True, to='blog.Comment', null=True)),
                ('user', models.ForeignKey(verbose_name=b'User', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comment',
            },
        ),
    ]
