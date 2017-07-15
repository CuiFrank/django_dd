# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermaininfo',
            name='state',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ordermaininfo',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
