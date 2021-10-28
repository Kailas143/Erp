# Generated by Django 3.2.8 on 2021-10-28 06:40

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('address_line1', models.CharField(max_length=1024, null=True)),
                ('address_line2', models.CharField(max_length=1024, null=True)),
                ('address_line3', models.CharField(max_length=1024, null=True)),
                ('office_email', models.CharField(blank=True, max_length=1024, null=True)),
                ('office_pnone_no', models.CharField(blank=True, max_length=1024, null=True)),
                ('gst_no', models.CharField(blank=True, max_length=1024, null=True)),
                ('acc_no', models.CharField(blank=True, max_length=1024, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=1024, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('purchase_company', models.BooleanField(default=True)),
                ('ratings', models.IntegerField(null=True)),
                ('vendor_code', models.CharField(blank=True, max_length=1024, null=True)),
                ('description', models.TextField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='job_components_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=1024, null=True)),
                ('c_code', models.CharField(max_length=1024, null=True)),
                ('c_unit', models.CharField(max_length=1024, null=True)),
                ('c_material_grade', models.CharField(max_length=1024, null=True)),
                ('qty_req', models.FloatField(null=True)),
                ('c_model_name', models.CharField(max_length=1024, null=True)),
                ('rotor_shaft', models.BooleanField(default=False)),
                ('shaft', models.BooleanField(default=False)),
                ('rotor', models.BooleanField(default=False)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='job_order_company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1024, null=True)),
                ('address_line1', models.CharField(max_length=1024, null=True)),
                ('address_line2', models.CharField(max_length=1024, null=True)),
                ('address_line3', models.CharField(max_length=1024, null=True)),
                ('office_email', models.CharField(max_length=1024, null=True)),
                ('office_pnone_no', models.CharField(max_length=1024, null=True)),
                ('gst_no', models.CharField(max_length=1024, null=True)),
                ('acc_no', models.CharField(max_length=1024, null=True)),
                ('ifsc_code', models.CharField(max_length=1024, null=True)),
                ('bank_name', models.CharField(max_length=1024, null=True)),
                ('branch_name', models.CharField(max_length=1024, null=True)),
                ('job_work_code', models.CharField(max_length=1024, null=True)),
                ('ratings', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='raw_components_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=1024, null=True)),
                ('c_code', models.CharField(max_length=1024, null=True)),
                ('c_unit', models.CharField(max_length=1024, null=True)),
                ('c_material_grade', models.CharField(max_length=1024, null=True)),
                ('c_model_name', models.CharField(max_length=1024, null=True)),
                ('wire', models.BooleanField(default=False)),
                ('winding', models.BooleanField(default=False)),
                ('shaft', models.BooleanField(default=False)),
                ('financial_year', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'PO'), (2, 'QC_HEAD'), (3, 'QC_WORKER'), (4, 'STORE'), (5, 'WINDING_STORE'), (6, 'WINDING_JOBORDER'), (7, 'WINDING_PRODUCTION'), (8, 'JOBORDER'), (9, 'ADMIN'), (10, 'GM_ACCESS'), (11, 'PRODUCTION_HEAD'), (12, 'PRODUCTION_SECTION1'), (13, 'PRODUCTION_TESTING'), (14, 'PRODUCTION_PACKING')], primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=1025, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='supliers_contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=1024, null=True)),
                ('phone_no', models.CharField(max_length=1024, null=True)),
                ('name', models.CharField(max_length=1024, null=True)),
                ('post', models.CharField(max_length=1024, null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('company_details', models.ForeignKey(blank=True, db_column='company_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='master.company_details')),
            ],
        ),
        migrations.CreateModel(
            name='raw_components_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_sgst', models.FloatField(max_length=1024, null=True)),
                ('c_cgst', models.FloatField(max_length=1024, null=True)),
                ('c_igst', models.FloatField(max_length=1024, null=True)),
                ('price', models.FloatField(null=True)),
                ('debit_price', models.FloatField(null=True)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('expire', models.BooleanField(default=False)),
                ('financial_year', models.DateField(auto_now=True)),
                ('company_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.company_details')),
                ('raw_components_details', models.ForeignKey(blank=True, db_column='c_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='master.raw_components_details')),
            ],
        ),
        migrations.CreateModel(
            name='job_order_supliers_contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=1024, null=True)),
                ('phone_no', models.CharField(max_length=1024, null=True)),
                ('name', models.CharField(max_length=1024, null=True)),
                ('post', models.CharField(max_length=1024, null=True)),
                ('financial_year', models.DateField(auto_now=True)),
                ('supliers_details', models.ForeignKey(blank=True, db_column='job_order_company_details', null=True, on_delete=django.db.models.deletion.CASCADE, to='master.job_order_company_details')),
            ],
        ),
        migrations.CreateModel(
            name='job_order_price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_sgst', models.IntegerField(null=True)),
                ('c_cgst', models.IntegerField(null=True)),
                ('c_igst', models.IntegerField(null=True)),
                ('price', models.FloatField(null=True)),
                ('debit_price', models.FloatField(null=True)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('expire', models.BooleanField(default=False)),
                ('financial_year', models.DateField(auto_now=True)),
                ('job_components_details', models.ForeignKey(blank=True, db_column='c_code', null=True, on_delete=django.db.models.deletion.CASCADE, to='master.job_components_details')),
                ('job_order_company_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.job_order_company_details')),
            ],
        ),
        migrations.AddField(
            model_name='job_components_details',
            name='raw_components_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.raw_components_details'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('admin_user', models.BooleanField(default=False)),
                ('status', models.IntegerField(null=True)),
                ('user_type', models.IntegerField(null=True)),
                ('profession', models.CharField(max_length=1025, null=True)),
                ('phone_no', models.BigIntegerField(null=True)),
                ('per_to_contact', models.CharField(max_length=1025, null=True)),
                ('contact_per_phone_no', models.BigIntegerField(null=True)),
                ('address_l1', models.TextField(null=True)),
                ('address_l2', models.TextField(null=True)),
                ('city', models.CharField(max_length=1025, null=True)),
                ('state', models.CharField(max_length=1025, null=True)),
                ('country', models.CharField(max_length=1025, null=True)),
                ('postcode', models.IntegerField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('roles', models.ManyToManyField(to='master.Role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]