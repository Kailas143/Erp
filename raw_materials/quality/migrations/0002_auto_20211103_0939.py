# Generated by Django 3.2.8 on 2021-11-03 04:09

from django.db import migrations, models
import django.db.models.deletion
import quality.models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0001_initial'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='inspection_report_details_raw_materials',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('tenant_id', models.PositiveIntegerField()),
        #         ('raw_material_fin_material_bill_inward', models.PositiveIntegerField(null=True)),
        #         ('raw_material_fin_material_dc_inward', models.PositiveIntegerField(null=True)),
        #         ('report_no', models.CharField(default=quality.models.reportnumber, max_length=1024, null=True)),
        #         ('inspection_date_start', models.DateTimeField(blank=True, null=True)),
        #         ('inspection_date_end', models.DateTimeField(blank=True, null=True)),
        #         ('sample_size', models.FloatField(null=True)),
        #         ('accepted_no', models.FloatField(null=True)),
        #         ('accepted_with_deviation_no', models.FloatField(null=True)),
        #         ('rejection_no', models.FloatField(null=True)),
        #         ('test_report', models.BooleanField(default=False)),
        #         ('status', models.BooleanField(blank=True, null=True)),
        #         ('statusreport', models.CharField(blank=True, choices=[(1, 'OK'), (2, 'REJECTED')], max_length=100, null=True)),
        #         ('financial_year', models.DateField(auto_now=True)),
        #         ('worker_name', models.CharField(max_length=1024)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='inspection_report_rows_raw_materials',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('tenant_id', models.PositiveIntegerField()),
        #         ('no_of_sample', models.IntegerField(null=True)),
        #         ('smp_no', models.IntegerField(null=True)),
        #         ('parameter_required', models.CharField(max_length=30, null=True)),
        #         ('val', models.FloatField(null=True)),
        #         ('statusreport', models.CharField(blank=True, choices=[(1, 'ok'), (2, 'not ok'), (3, 'tested partially')], max_length=100, null=True)),
        #         ('worker_name', models.CharField(max_length=1024)),
        #         ('financial_year', models.DateField(auto_now=True)),
        #         ('inspection_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quality.inspection_report_details_raw_materials')),
        #     ],
        # ),
        # migrations.AddField(
        #     model_name='parameters',
        #     name='financial_year',
        #     field=models.DateField(auto_now=True),
        # ),
        # migrations.AddField(
        #     model_name='parameters',
        #     name='tenant_id',
        #     field=models.PositiveIntegerField(default=1),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='parameters',
        #     name='worker_name',
        #     field=models.CharField(default=1, max_length=1024),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='remarks',
        #     name='financial_year',
        #     field=models.DateField(auto_now=True),
        # ),
        # migrations.AddField(
        #     model_name='remarks',
        #     name='tenant_id',
        #     field=models.PositiveIntegerField(default=1),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='remarks',
        #     name='worker_name',
        #     field=models.CharField(default=1, max_length=1024),
        #     preserve_default=False,
        # ),
        # migrations.DeleteModel(
        #     name='inspection_report_rows',
        # ),
        # migrations.AlterField(
        #     model_name='remarks',
        #     name='inspection_report',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quality.inspection_report_details_raw_materials'),
        # ),
        # migrations.DeleteModel(
        #     name='inspection_report_details',
        # ),
    ]
