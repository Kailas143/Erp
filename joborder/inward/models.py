from django.db import models
import datetime

# Create your models here.
class FinancialQuerySet(models.QuerySet):
    def current_financialyear(self):
        year = datetime.datetime.now().year
        current_finyear_start= datetime.datetime(year, 4, 1)#current_finyear_start 2021
        current_finyear_end= datetime.datetime(year+1, 3, 31)#current_finyear_end 2022
        return self.filter(financial_period__gte=current_finyear_start,financial_period__lte=current_finyear_end,tenant_id=1)

class joborder_fin_bill_inward_details(models.Model):
    tenant_id=models.PositiveIntegerField()
    bill_no =  models.CharField(null=True,max_length=1024)
    inward_date_time =  models.DateTimeField(null=True)
    bill_date = models.DateField(null=True)
    job_order_company_details =  models.PositiveIntegerField()
    extra = models.FloatField(null=True)
    bill_amt=models.FloatField(null=True)
    t_amount = models.FloatField(null=True)
    t_gst=models.FloatField(null=True)
    igst_amount=models.FloatField(null=True)
    sgst_amount = models.FloatField(null=True)
    cgst_amount = models.FloatField(null=True)
    direct_bill = models.BooleanField(default=False)
    dc_reff = models.BooleanField(default=False)
    qc_bill_check=models.BooleanField(default=False)
    qc_check = models.BooleanField(default=False)
    receipt_no = models.IntegerField(null=True)
    recived_by = models.CharField(null=True,max_length=1024)
    financial_year = models.DateField(auto_now=True)
    worker_name=models.CharField(max_length=1024)

    objects = FinancialQuerySet.as_manager()
    def __str__(self):
        return str(self.bill_no) + '  -  ' + str(self.job_order_company_details) + '  -  ' + str(self.inward_date_time)

class receipt_no_generation(models.Model):
    tenant_id=models.PositiveIntegerField()
    receipt_no=models.IntegerField(null=True)
    financial_year = models.DateField(auto_now=True)
    worker_name=models.CharField(max_length=1024)

    objects = FinancialQuerySet.as_manager()
    def __str__(self):
        return str(self.receipt_no) + '  -  ' + str(self.id)

class joborder_fin_material_bill_inward(models.Model):
    tenant_id=models.PositiveIntegerField()
    joborder_fin_bill_inward_details=models.ForeignKey(joborder_fin_bill_inward_details, null=True, blank=True, on_delete=models.CASCADE)
    job_order_price = models.PositiveIntegerField()
    qty =  models.IntegerField(null=True)
    billed_qty = models.IntegerField(null=True)
    rate_match = models.BooleanField(default=True)
    error  = models.IntegerField(null=True)
    error_bal = models.IntegerField(null=True)
    igst_amount=models.FloatField(null=True)
    sgst_amount = models.FloatField(null=True)
    cgst_amount = models.FloatField(null=True)
    tgst=models.FloatField(null=True)
    bill_amount=models.FloatField(null=True)
    debit_note_rised = models.BooleanField(default=False)
    debit_note_no = models.IntegerField(null=True)
    financial_year = models.DateField(auto_now=True)
    worker_name=models.CharField(max_length=1024)

    objects = FinancialQuerySet.as_manager()
    def __str__(self):
        return str(self.job_order_price) + '  -  ' + str(self.qty) + '  -  ' + str(self.rate_match)

class joborder_fin_dc_inward_details(models.Model):
    tenant_id=models.PositiveIntegerField()
    dc_no =  models.CharField(null=True,max_length=1024)
    inward_date_time =  models.DateTimeField(null=True)
    dc_date = models.DateField(null=True)
    job_order_company_details = models.PositiveIntegerField()
    bill_reff = models.ForeignKey(joborder_fin_bill_inward_details, null=True, blank=True, on_delete=models.CASCADE)
    bill_reff_true = models.BooleanField(default=False)
    qc_dc_check = models.BooleanField(default=False)
    qc_check = models.BooleanField(default=False)
    receipt_no = models.IntegerField(null=True)
    recived_by = models.IntegerField(null=True)
    financial_year = models.DateField(auto_now=True)
    worker_name=models.CharField(max_length=1024)

    objects = FinancialQuerySet.as_manager()
    def __str__(self):
        return str(self.dc_no) + '  -  ' + str(self.job_order_company_details) + '  -  ' + str(self.id)

class joborder_fin_material_dc_inward(models.Model):
    tenant_id=models.PositiveIntegerField()
    joborder_fin_dc_inward_details=models.ForeignKey(joborder_fin_dc_inward_details, null=True, blank=True, on_delete=models.CASCADE)
    job_order_price = models.PositiveIntegerField()
    qty =  models.IntegerField(null=True)
    billed_qty = models.IntegerField(null=True)
    error = models.IntegerField(null=True)
    financial_year = models.DateField(auto_now=True)
    worker_name=models.CharField(max_length=1024)

    objects = FinancialQuerySet.as_manager()
    def __str__(self):
        return str(self.joborder_fin_dc_inward_details) + '  -  ' + str(self.qty) + '  -  ' + str(self.id)