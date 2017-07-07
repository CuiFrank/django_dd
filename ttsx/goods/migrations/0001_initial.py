# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(null=True, max_length=100)),
                ('pic', models.ImageField(upload_to='goods/', default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('click', models.IntegerField(default=0, null=True)),
                ('unit', models.CharField(null=True, max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('sub_title', models.CharField(max_length=200)),
                ('rest', models.IntegerField(default=100)),
                ('detail', tinymce.models.HTMLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='KindsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('kinds', models.CharField(max_length=20)),
                ('rest', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='type',
            field=models.ForeignKey(to='goods.KindsInfo'),
        ),
    ]
