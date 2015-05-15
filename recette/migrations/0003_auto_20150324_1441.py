# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0002_auto_20150324_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type_recette',
            old_name='type',
            new_name='type_recette',
        ),
    ]
