# Generated by Django 2.2.6 on 2019-10-24 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_identifier", "0002_auto_20190305_0123")]

    operations = [
        migrations.AlterField(
            model_name="identifiermodel",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="sites.Site",
            ),
        )
    ]
