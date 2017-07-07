# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='code',
            field=models.CharField(max_length=6, default=''),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=11, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='passwd',
            field=models.CharField(max_length=40),
        ),
    ]
