# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDetails', '0003_auto_20171112_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersocialnetworks',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='membersocialnetworks',
            name='github',
            field=models.CharField(blank=True, max_length=100, verbose_name='Github'),
        ),
        migrations.AlterField(
            model_name='membersocialnetworks',
            name='googleplus',
            field=models.CharField(blank=True, max_length=100, verbose_name='GooglePlus'),
        ),
        migrations.AlterField(
            model_name='membersocialnetworks',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, verbose_name='LinkedIn'),
        ),
        migrations.AlterField(
            model_name='membersocialnetworks',
            name='stackoverflow',
            field=models.CharField(blank=True, max_length=100, verbose_name='Stackoverflow'),
        ),
        migrations.AlterField(
            model_name='membersocialnetworks',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, verbose_name='Twitter'),
        ),
    ]
