# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='name',
        ),
    ]
