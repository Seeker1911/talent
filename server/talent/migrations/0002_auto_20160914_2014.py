# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='song',
            old_name='owner',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='name',
            new_name='title',
        ),
    ]