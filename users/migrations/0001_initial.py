# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('gender', models.CharField(max_length=2, choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')])),
            ],
        ),
    ]
