# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20171201_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='links',
            field=models.ManyToManyField(blank=True, to='books.Link'),
        ),
    ]