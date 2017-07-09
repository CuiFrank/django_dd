# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0005_cartinfo_goods_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartinfo',
            name='goods_id',
            field=models.IntegerField(default=200),
        ),
    ]
