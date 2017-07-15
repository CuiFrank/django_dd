# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0002_auto_20170714_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermaininfo',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]
