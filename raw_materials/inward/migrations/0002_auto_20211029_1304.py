# Generated by Django 3.2.8 on 2021-10-29 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inward', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raw_component_fin_bill_inward_details',
            old_name='job_order_company_details',
            new_name='raw_component_company_details',
        ),
        migrations.RenameField(
            model_name='raw_component_fin_dc_inward_details',
            old_name='job_order_company_details',
            new_name='raw_component_company_details',
        ),
        migrations.RenameField(
            model_name='raw_component_fin_material_bill_inward',
            old_name='job_order_price',
            new_name='raw_component_price',
        ),
    ]