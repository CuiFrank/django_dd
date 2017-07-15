# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0003_ordermaininfo_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetailinfo',
            name='tot_one',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
