# Generated by Django 3.2.8 on 2021-10-29 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='joborder_fin_bill_inward_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.CharField(max_length=1024, null=True)),
                ('inward_date_time', models.DateTimeField(null=True)),
                ('bill_date', models.DateField(null=True)),
                ('job_order_company_details', models.PositiveIntegerField()),
                ('extra', models.FloatField(null=True)),
                ('bill_amt', models.FloatField(null=True)),
                ('t_amount', models.FloatField(null=True)),
                ('t_gst', models.FloatField(null=True)),
                ('igst_amount', models.FloatField(null=True)),
                ('sgst_amount', models.FloatField(null=True)),
                ('cgst_amount', models.FloatField(null=True)),
                ('direct_bill', models.BooleanField(default=False)),
                ('dc_reff', models.BooleanField(default=False)),
                ('qc_bill_check', models.BooleanField(default=False)),
                ('qc_check', models.BooleanField(default=False)),
                ('receipt_no', models.IntegerField(null=True)),
                ('recived_by', models.CharField(max_length=1024, null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('worker_name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='joborder_fin_dc_inward_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_no', models.CharField(max_length=1024, null=True)),
                ('inward_date_time', models.DateTimeField(null=True)),
                ('dc_date', models.DateField(null=True)),
                ('job_order_company_details', models.PositiveIntegerField()),
                ('bill_reff_true', models.BooleanField(default=False)),
                ('qc_dc_check', models.BooleanField(default=False)),
                ('qc_check', models.BooleanField(default=False)),
                ('receipt_no', models.IntegerField(null=True)),
                ('recived_by', models.IntegerField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('worker_name', models.CharField(max_length=1024)),
                ('bill_reff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inward.joborder_fin_bill_inward_details')),
            ],
        ),
        migrations.CreateModel(
            name='receipt_no_generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_no', models.IntegerField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('worker_name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='joborder_fin_material_dc_inward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_order_price', models.PositiveIntegerField()),
                ('qty', models.IntegerField(null=True)),
                ('billed_qty', models.IntegerField(null=True)),
                ('error', models.IntegerField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('worker_name', models.CharField(max_length=1024)),
                ('joborder_fin_dc_inward_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inward.joborder_fin_dc_inward_details')),
            ],
        ),
        migrations.CreateModel(
            name='joborder_fin_material_bill_inward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_order_price', models.PositiveIntegerField()),
                ('qty', models.IntegerField(null=True)),
                ('billed_qty', models.IntegerField(null=True)),
                ('rate_match', models.BooleanField(default=True)),
                ('error', models.IntegerField(null=True)),
                ('error_bal', models.IntegerField(null=True)),
                ('igst_amount', models.FloatField(null=True)),
                ('sgst_amount', models.FloatField(null=True)),
                ('cgst_amount', models.FloatField(null=True)),
                ('tgst', models.FloatField(null=True)),
                ('bill_amount', models.FloatField(null=True)),
                ('debit_note_rised', models.BooleanField(default=False)),
                ('debit_note_no', models.IntegerField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('worker_name', models.CharField(max_length=1024)),
                ('joborder_fin_bill_inward_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inward.joborder_fin_bill_inward_details')),
            ],
        ),
    ]
