# Generated by Django 5.0.2 on 2024-02-27 05:39

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0009_alter_customercomplaints_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.IntegerField(null=True, verbose_name='row_id')),
                ('psp_id', models.CharField(max_length=10, null=True, verbose_name='psp_id')),
                ('agent_id', models.CharField(max_length=10, null=True, unique=True, verbose_name='agent_id')),
                ('reporting_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='reporting_date')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Coporate')], max_length=5, verbose_name='gender')),
            ],
        ),
        migrations.RemoveField(
            model_name='customercomplaints',
            name='agent_id',
        ),
        migrations.RemoveField(
            model_name='customercomplaints',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customercomplaints',
            name='psp_id',
        ),
        migrations.RemoveField(
            model_name='customercomplaints',
            name='row_id',
        ),
        migrations.RemoveField(
            model_name='scheduleddirectors',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='scheduleddirectors',
            name='psp_id',
        ),
        migrations.RemoveField(
            model_name='scheduleddirectors',
            name='reporting_date',
        ),
        migrations.RemoveField(
            model_name='scheduleddirectors',
            name='row_id',
        ),
        migrations.AddField(
            model_name='customercomplaints',
            name='complaints',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='samples.abstractmodel', verbose_name='customer'),
        ),
        migrations.AddField(
            model_name='scheduleddirectors',
            name='complaints',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='samples.abstractmodel', verbose_name='customer'),
        ),
        migrations.CreateModel(
            name='MobileInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_cell', models.CharField(max_length=10, verbose_name='favorite_cell')),
                ('sub_county_code', models.CharField(max_length=3, verbose_name='sub_county_code')),
                ('agent_type_code', models.CharField(max_length=10, verbose_name='agent_type_code')),
                ('agent_status', models.CharField(choices=[('A', 'Active'), ('D', 'Dormant')], max_length=25, verbose_name='agent_status')),
                ('band_code', models.CharField(max_length=25, verbose_name='band_code')),
                ('cash_in_volume', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='cash_volume')),
                ('value_cash_in', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='value_cash_in')),
                ('cash_out_volume', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='cash_out_volume')),
                ('value_cash_out', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='value_cash_out')),
                ('float_amount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='float_amount')),
                ('agent_cash_deposits', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='agent_cash_deposits')),
                ('agent_cash_deposits_bank', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='agent_cash_deposits_bank')),
                ('agent_cash_withdrawal_bank', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='agent_cash_withdrawal_bank')),
                ('value_agent_cash_withdrawal_bank', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='value_agent_cash_withdrawal_bank')),
                ('complaints', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='samples.abstractmodel', verbose_name='customer')),
            ],
        ),
    ]