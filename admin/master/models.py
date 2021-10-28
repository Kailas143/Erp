import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class financial_year_manager(models.QuerySet):
   def current_financial_year(self):
        return self.filter(financial_year__gte=datetime.date(2021,4,1),financial_year__lte=datetime.date(2022,3,31))

YEAR_MANAGER = models.Manager.from_queryset(financial_year_manager)

### user roles

class Role(models.Model):
  PO = 1
  QC_HEAD = 2
  QC_WORKER = 3
  STORE = 4
  WINDING_STORE = 5
  WINDING_JOBORDER = 6
  WINDING_PRODUCTION = 7
  JOBORDER = 8
  ADMIN = 9
  GM_ACCESS = 10
  PRODUCTION_HEAD= 11
  PRODUCTION_SECTION1 = 12
  PRODUCTION_TESTING = 13
  PRODUCTION_PACKING = 14
  ROLE_CHOICES = (
      (PO, 'PO'),
      (QC_HEAD, 'QC_HEAD'),
      (QC_WORKER, 'QC_WORKER'),
      (STORE, 'STORE'),
      (WINDING_STORE, 'WINDING_STORE'),
      (WINDING_JOBORDER, 'WINDING_JOBORDER'),
      (WINDING_PRODUCTION, 'WINDING_PRODUCTION'),
      (JOBORDER, 'JOBORDER'),
      (ADMIN, 'ADMIN'),
      (GM_ACCESS, 'GM_ACCESS'),
      (PRODUCTION_HEAD, 'PRODUCTION_HEAD'),
      (PRODUCTION_SECTION1, 'PRODUCTION_SECTION1'),
      (PRODUCTION_TESTING, 'PRODUCTION_TESTING'),
      (PRODUCTION_PACKING, 'PRODUCTION_PACKING'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
  value = models.CharField(null=True, max_length=1025)

  def __str__(self):
      return self.get_id_display()


class User(AbstractUser):
  roles = models.ManyToManyField(Role)
  admin_user = models.BooleanField(default=False)
  status = models.IntegerField(null=True)
  user_type = models.IntegerField(null=True)
  profession = models.CharField(null=True, max_length=1025)
  phone_no = models.BigIntegerField(null=True)
  per_to_contact =  models.CharField(null=True, max_length=1025)
  contact_per_phone_no = models.BigIntegerField(null=True)
  address_l1 = models.TextField(null=True)
  address_l2 = models.TextField(null=True)
  city = models.CharField(null=True, max_length=1025)
  state = models.CharField(null=True, max_length=1025)
  country = models.CharField(null=True, max_length=1025)
  postcode = models.IntegerField(null=True)

  def __str__(self):
      return str(self.username) + '  -  ' + str(self.status)+ '  -  ' + str(self.id)

  #####################################


class company_details(models.Model):
    company_name = models.CharField(null=True,blank=True, max_length=1024)
    address_line1 = models.CharField(null=True, max_length=1024)
    address_line2 = models.CharField(null=True, max_length=1024)
    address_line3 = models.CharField(null=True, max_length=1024)
    office_email = models.CharField(null=True,blank=True, max_length=1024)
    office_pnone_no = models.CharField(null=True,blank=True, max_length=1024)
    gst_no = models.CharField(null=True,blank=True, max_length=1024)
    acc_no = models.CharField(null=True,blank=True, max_length=1024)
    ifsc_code = models.CharField(null=True,blank=True, max_length=1024)
    bank_name = models.CharField(null=True,blank=True, max_length=1024)
    branch_name = models.CharField(null=True,blank=True, max_length=1024)
    purchase_company = models.BooleanField(default=True)
    ratings=models.IntegerField(null=True)
    vendor_code=models.CharField(null=True,blank=True, max_length=1024)
    description = models.TextField(null=True)
    financial_year = models.DateField(auto_now=True)

    objects = YEAR_MANAGER()
    def __str__(self):
        return str(self.company_name) + '  -  ' + str(self.purchase_company) + '  -  ' + str(self.gst_no) + '  -  ' + str(self.id)

class supliers_contact_details(models.Model):
    company_details = models.ForeignKey(company_details, null=True, db_column='company_name', blank=True, on_delete=models.CASCADE)
    email = models.CharField(null=True, max_length=1024)
    phone_no = models.CharField(null=True, max_length=1024)
    name = models.CharField(null=True, max_length=1024)
    post = models.CharField(null=True, max_length=1024)
    financial_year = models.DateField(auto_now=True)

    objects = YEAR_MANAGER()
    def __str__(self):
        return str(self.company_details) + '  -  ' + str(self.name) + '  -  ' + str(self.phone_no)+ '  -  ' + str(self.post)

class job_order_company_details(models.Model):
    company_name = models.CharField(null=True, max_length=1024)
    address_line1 = models.CharField(null=True, max_length=1024)
    address_line2 = models.CharField(null=True, max_length=1024)
    address_line3 = models.CharField(null=True, max_length=1024)
    office_email = models.CharField(null=True, max_length=1024)
    office_pnone_no = models.CharField(null=True, max_length=1024)
    gst_no = models.CharField(null=True, max_length=1024)
    acc_no = models.CharField(null=True, max_length=1024)
    ifsc_code = models.CharField(null=True, max_length=1024)
    bank_name = models.CharField(null=True, max_length=1024)
    branch_name = models.CharField(null=True, max_length=1024)
    job_work_code = models.CharField(null=True, max_length=1024)
    ratings = models.IntegerField(null=True)
    description = models.TextField(null=True)
    financial_year = models.DateField(auto_now=True)

    objects = YEAR_MANAGER()
    def __str__(self):
        return str(self.company_name) + '  -  ' + str(self.gst_no) + '  -  ' + str(self.job_work_code)

class job_order_supliers_contact_details(models.Model):
    supliers_details = models.ForeignKey(job_order_company_details, null=True, db_column='job_order_company_details', blank=True, on_delete=models.CASCADE)
    email = models.CharField(null=True, max_length=1024)
    phone_no = models.CharField(null=True, max_length=1024)
    name = models.CharField(null=True, max_length=1024)
    post = models.CharField(null=True, max_length=1024)
    financial_year = models.DateField(auto_now=True)

    objects = YEAR_MANAGER()
    def __str__(self):
        return str(self.supliers_details) + '  -  ' + str(self.name) + '  -  ' + str(self.phone_no)+ '  -  ' + str(self.post)


class raw_components_details(models.Model):
    c_name = models.CharField(null=True, max_length=1024)
    c_code = models.CharField(null=True, max_length=1024)
    c_unit = models.CharField(null=True, max_length=1024)
    c_material_grade = models.CharField(null=True, max_length=1024)
    c_model_name = models.CharField(null=True, max_length=1024)
    wire = models.BooleanField(default=False)
    winding = models.BooleanField(default=False)
    shaft = models.BooleanField(default=False)
    financial_year = models.DateField(auto_now=True)

    objects = YEAR_MANAGER()
    def __str__(self):
        return str(self.c_code) + '  -  ' + str(self.c_name) + '  -  ' + str(self.c_material_grade)

class raw_components_price(models.Model):
    company_details = models.ForeignKey(company_details, null=True, blank=True, on_delete=models.CASCADE)
    raw_components_details = models.ForeignKey(raw_components_details, null=True, db_column='c_code', blank=True, on_delete=models.CASCADE)
    c_sgst = models.FloatField(null=True, max_length=1024)
    c_cgst = models.FloatField(null=True, max_length=1024)
    c_igst = models.FloatField(null=True, max_length=1024)
    price = models.FloatField(null=True)
    debit_price = models.FloatField(null=True)
    expire_date = models.DateTimeField(null=True,blank=True)
    expire = models.BooleanField(default=False)
    financial_year = models.DateField(auto_now=True)

    objects = YEAR_MANAGER()
    def __str__(self):
        return str(self.company_details) + '  -  ' + str(self.raw_components_details) + '  -  ' + str(self.price)

class job_components_details(models.Model):
    c_name = models.CharField(null=True, max_length=1024)
    c_code = models.CharField(null=True, max_length=1024)
    c_unit = models.CharField(null=True, max_length=1024)
    c_material_grade = models.CharField(null=True, max_length=1024)
    raw_components_details = models.ForeignKey(raw_components_details, null=True, blank=True, on_delete=models.CASCADE)
    qty_req = models.FloatField(null=True)
    c_model_name = models.CharField(null=True, max_length=1024)
    rotor_shaft = models.BooleanField(default=False)
    shaft = models.BooleanField(default=False)
    rotor = models.BooleanField(default=False)
    financial_year = models.DateField(auto_now=True)

    objects = YEAR_MANAGER()
    def __str__(self):
        return str(self.c_code) + '  -  ' + str(self.c_name) + '  -  ' + str(self.id)

class job_order_price(models.Model):
    job_order_company_details = models.ForeignKey(job_order_company_details, null=True, blank=True, on_delete=models.CASCADE)
    job_components_details = models.ForeignKey(job_components_details, null=True, db_column='c_code', blank=True, on_delete=models.CASCADE)
    c_sgst = models.IntegerField(null=True)
    c_cgst = models.IntegerField(null=True)
    c_igst = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    debit_price = models.FloatField(null=True)
    expire_date = models.DateTimeField(null=True,blank=True)
    expire = models.BooleanField(default=False)
    financial_year = models.DateField(auto_now=True)

    objects = YEAR_MANAGER()
    def __str__(self):
        return str(self.job_order_company_details) + '  -  ' + str(self.job_components_details) + '  -  ' + str(self.price)