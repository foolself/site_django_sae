# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'category_name')),
                ('index', models.IntegerField(default=999, verbose_name=b'category_index')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'tag_name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tag',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name=b'Content'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name=b'Category', blank=True, to='blog.Category', null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name=b'Tag'),
        ),
    ]
