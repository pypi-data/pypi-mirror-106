# Generated by Django 2.0.1 on 2018-01-16 13:28

import django.db.models.deletion
import edc_sites.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("edc_reference", "0003_reference_related_name"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="reference",
            managers=[("on_site", edc_sites.models.CurrentSiteManager())],
        ),
        migrations.AddField(
            model_name="reference",
            name="site",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="sites.Site",
            ),
        ),
    ]
