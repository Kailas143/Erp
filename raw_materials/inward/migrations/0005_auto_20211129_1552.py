# Generated by Django 3.2.8 on 2021-11-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inward', '0004_auto_20211029_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raw_component_fin_bill_inward_details',
            name='tenant_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='raw_component_fin_dc_inward_details',
            name='tenant_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='raw_component_fin_material_bill_inward',
            name='tenant_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='raw_component_fin_material_dc_inward',
            name='tenant_id',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='receipt_no_generation',
            name='tenant_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
