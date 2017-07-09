# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0003_postinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('pic', models.ImageField(default='', upload_to='goods/')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2, null=True)),
                ('unit', models.CharField(max_length=20, null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('num', models.IntegerField(default=0)),
                ('total', models.DecimalField(max_digits=12, decimal_places=2)),
                ('user', models.ForeignKey(to='df_user.UserInfo')),
            ],
        ),
    ]
