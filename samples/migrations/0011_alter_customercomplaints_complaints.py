# Generated by Django 5.0.2 on 2024-02-27 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0010_abstractmodel_remove_customercomplaints_agent_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercomplaints',
            name='complaints',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='samples.abstractmodel'),
        ),
    ]
