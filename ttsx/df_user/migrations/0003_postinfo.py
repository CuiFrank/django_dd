# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_auto_20170705_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('post_addr', models.CharField(default='', max_length=100)),
                ('post_phone', models.CharField(default='', max_length=11)),
                ('post_code', models.CharField(default='', max_length=6)),
                ('post_name', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
    ]
