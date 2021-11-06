# Generated by Django 3.2.8 on 2021-11-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0007_remove_inspection_report_details_financial_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='inspection_report_rows',
            name='financial_year',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='parameters',
            name='financial_year',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='remarks',
            name='financial_year',
            field=models.DateField(auto_now=True),
        ),
    ]
