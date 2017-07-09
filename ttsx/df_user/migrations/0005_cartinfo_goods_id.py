# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0004_cartinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartinfo',
            name='goods_id',
            field=models.IntegerField(default=0),
        ),
    ]
