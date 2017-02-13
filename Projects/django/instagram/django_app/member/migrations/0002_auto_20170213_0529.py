# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='follower_set', to='member.MyUser'),
        ),
    ]
