# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ext_auth', '0002_auto_20210430_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='externaluseridentifier',
            name='app_id',
            field=models.CharField(default=b'', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
    ]
