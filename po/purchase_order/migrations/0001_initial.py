# Generated by Django 3.2.8 on 2021-10-29 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='excess_po_verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('raw_components_details', models.PositiveIntegerField()),
                ('store_min', models.IntegerField(null=True)),
                ('store_max', models.IntegerField(null=True)),
                ('store_bal', models.IntegerField(null=True)),
                ('po_bal', models.IntegerField(null=True)),
                ('draft_bal', models.IntegerField(null=True)),
                ('reson', models.TextField(blank=True, null=True)),
                ('permission', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='mail_recived_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('sender_details', models.PositiveIntegerField()),
                ('email_user_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('mail_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('mail_subject', models.CharField(blank=True, max_length=1024, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('mail_discuss', models.BooleanField(default=False)),
                ('auto_reff', models.BooleanField(default=False)),
                ('uncat', models.BooleanField(default=False)),
                ('po_refff', models.BooleanField(default=False)),
                ('rate_refff', models.BooleanField(default=False)),
                ('unwanted', models.BooleanField(default=False)),
                ('reffrenece_user', models.CharField(max_length=102, null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='mail_recived_details_po_cancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('sender_details', models.PositiveIntegerField()),
                ('email_user_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('mail_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('mail_subject', models.CharField(blank=True, max_length=1024, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='mail_sent_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('recivers_details', models.PositiveIntegerField()),
                ('email_user_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('mail_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('mail_subject', models.CharField(blank=True, max_length=1024, null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='mail_sent_details_po_cancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('recivers_details', models.PositiveIntegerField()),
                ('email_user_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('mail_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('mail_subject', models.CharField(blank=True, max_length=1024, null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='po_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('supliers_details', models.PositiveIntegerField()),
                ('po_no', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('mail_date', models.DateField(null=True)),
                ('bill_amt', models.FloatField(null=True)),
                ('t_amount', models.FloatField(null=True)),
                ('t_gst', models.FloatField(null=True)),
                ('igst_amount', models.FloatField(null=True)),
                ('sgst_amount', models.FloatField(null=True)),
                ('cgst_amount', models.FloatField(null=True)),
                ('draft', models.BooleanField(default=True)),
                ('gm_aprove', models.IntegerField(blank=True, null=True)),
                ('pro_aprove', models.IntegerField(blank=True, null=True)),
                ('admin_aprove', models.IntegerField(blank=True, null=True)),
                ('admin_check', models.BooleanField(default=False)),
                ('not_sent', models.BooleanField(default=True)),
                ('cancel', models.BooleanField(default=False)),
                ('send_status', models.IntegerField(blank=True, null=True)),
                ('recive_status', models.IntegerField(blank=True, null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='po_no_increment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('po_no', models.IntegerField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='raw_material_error_to_error_tally',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('raw_inward_for', models.IntegerField(null=True)),
                ('raw_inward_used', models.IntegerField(null=True)),
                ('for_qty_in', models.IntegerField(null=True)),
                ('for_qty_left', models.IntegerField(null=True)),
                ('used_qty_in', models.IntegerField(null=True)),
                ('used_qty_left', models.IntegerField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='recived_mail_po_reff_cancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('checked', models.BooleanField(default=False)),
                ('financial_year', models.DateField(auto_now=True)),
                ('mail_recived_details_po_cancel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.mail_recived_details_po_cancel')),
                ('mail_sent_details_po_cancel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.mail_sent_details_po_cancel')),
                ('po_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.po_details')),
            ],
        ),
        migrations.CreateModel(
            name='recived_mail_po_reff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('stauts', models.BooleanField(default=False)),
                ('checked', models.BooleanField(default=False)),
                ('resons', models.CharField(blank=True, max_length=1024, null=True)),
                ('withoutmail', models.BooleanField(default=False)),
                ('financial_year', models.DateField(auto_now=True)),
                ('mail_recived_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.mail_recived_details')),
                ('mail_sent_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.mail_sent_details')),
                ('po_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.po_details')),
            ],
        ),
        migrations.CreateModel(
            name='price_update_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('company_details', models.PositiveIntegerField()),
                ('raw_components_price', models.PositiveIntegerField()),
                ('quote_val', models.FloatField(null=True)),
                ('action', models.BooleanField(null=True)),
                ('admin_quote_val', models.FloatField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('mail_recived_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.mail_recived_details')),
            ],
        ),
        migrations.CreateModel(
            name='po_request_response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('role', models.CharField(blank=True, max_length=1024, null=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('rejected', models.BooleanField(default=False)),
                ('financial_year', models.DateField(auto_now=True)),
                ('po_details', models.ForeignKey(blank=True, db_column='po_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.po_details')),
            ],
        ),
        migrations.CreateModel(
            name='po_order_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('raw_components_price', models.PositiveIntegerField()),
                ('qty', models.IntegerField(null=True)),
                ('bal_qty', models.IntegerField(null=True)),
                ('bill_amt', models.FloatField(null=True)),
                ('igst_amount', models.FloatField(null=True)),
                ('sgst_amount', models.FloatField(null=True)),
                ('cgst_amount', models.FloatField(null=True)),
                ('tgst', models.FloatField(null=True)),
                ('t_amount', models.FloatField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('po_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.po_details')),
            ],
        ),
        migrations.CreateModel(
            name='order_schelude_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.PositiveIntegerField()),
                ('delivery_date', models.DateField(null=True)),
                ('qty', models.IntegerField(null=True)),
                ('bal_qty', models.IntegerField(null=True)),
                ('table_no', models.BooleanField(default=False)),
                ('financial_year', models.DateField(auto_now=True)),
                ('po_order_list', models.ForeignKey(blank=True, db_column='order', null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.po_order_list')),
            ],
        ),
        migrations.AddField(
            model_name='mail_sent_details_po_cancel',
            name='po_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.po_details'),
        ),
        migrations.AddField(
            model_name='mail_sent_details',
            name='po_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase_order.po_details'),
        ),
    ]
