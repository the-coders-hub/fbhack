# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.DecimalField(max_digits=3, decimal_places=1)),
                ('comment', models.TextField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
