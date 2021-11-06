from django.db import models

# Create your models here.
from django.db import models
import datetime

from django.db.models.fields import PositiveIntegerField

# Create your models here.


class finacialyear(models.QuerySet):
    def finpd(self):
        year = datetime.time.now().year
        startyear = datetime.datetime(year, 4, 1)
        endyear = datetime.datetime(year, 31, 3)
        return self.filter(finperiod_gte=startyear, finperiod_lte=endyear,tenant_id=1)


def reportnumber():
    lastreportnumber = inspection_report_details_job_order.objects.all().order_by('id').last()
    if not lastreportnumber :
        return 'RE0001'
    report_no = lastreportnumber.report_no
    report_no_int = int(report_no.split('E')[-1])
    
  
    newreportno_int=report_no_int +1
    newreportno = 'RE000' + str(newreportno_int)
    return newreportno

st=[(1,'OK'),(2,'REJECTED')]

class inspection_report_details_job_order(models.Model):
    tenant_id=models.PositiveIntegerField()
    joborder_fin_material_bill_inward = PositiveIntegerField(null=True)
    joborder_fin_material_dc_inward =PositiveIntegerField(null=True)
    report_no = models.CharField(max_length=1024,null=True,default=reportnumber)
    inspection_date_start = models.DateTimeField(null=True, blank=True)     
    inspection_date_end = models.DateTimeField(null=True, blank=True)
    sample_size=models.FloatField(null=True)
    accepted_no = models.FloatField(null=True)
    accepted_with_deviation_no = models.FloatField(null=True)
    rejection_no = models.FloatField(null=True)
    test_report = models.BooleanField(default=False)
    status = models.BooleanField(null=True, blank=True)
    statusreport=models.CharField(max_length=100,choices=st,null=True, blank=True)
    financial_year = models.DateField(auto_now=True)
    worker_name=models.CharField(max_length=1024)
    objects = finacialyear()


    def __str__(self):
        return self.report_no


class parameters(models.Model):
    
    tenant_id=models.PositiveIntegerField()
    field1= models.FloatField(null=True)
    field2 = models.FloatField(null=True)
    field3 = models.FloatField(null=True)
    field4 = models.FloatField(null=True)
    field5 = models.FloatField(null=True)
    financial_year = models.DateField(auto_now=True)
    worker_name=models.CharField(max_length=1024)
    
    objects = finacialyear()


    def __str__(self):
        return self.field1


sta=[(1,'ok'),(2,'not ok'),(3,'tested partially')]

class inspection_report_rows_job_order(models.Model):
    tenant_id=models.PositiveIntegerField()
    inspection_report = models.ForeignKey(inspection_report_details_job_order, null=True, blank=True, on_delete=models.CASCADE)
    no_of_sample = models.IntegerField(null=True)
    smp_no = models.IntegerField(null=True)
    parameter_required = models.CharField(max_length=30,null=True)
    val= models.FloatField(null=True)
    statusreport = models.CharField(max_length=100, choices=sta, null=True, blank=True)
    worker_name=models.CharField(max_length=1024)
    financial_year = models.DateField(auto_now=True)
    objects = finacialyear()

    def __str__(self):
        return str(self.smp_no)


remark_list=[(1,'list1'),(2,'list2'),(3,'list3'),(4,'list4'),(5,'list5')]
class remarks(models.Model):
    tenant_id=models.PositiveIntegerField()
    inspection_report = models.ForeignKey(inspection_report_details_job_order, null=True, blank=True, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=50, choices=remark_list, default=1)
    worker_name=models.CharField(max_length=1024)
    financial_year = models.DateField(auto_now=True)
    objects = finacialyear()

# class inspection_report_details_joborder(models.Model):
#     joborder_fin_material_bill_inward = PositiveIntegerField()
#     joborder_fin_material_dc_inward =PositiveIntegerField()
#     sample_plan_rows = models.ForeignKey(sample_plan_rows, null=True, blank=True, on_delete=models.CASCADE)
#     doc_no = models.CharField(null=True, max_length=1024)
#     report_no = models.CharField(null=True,default=reportnumber)
#     inspection_date_start = models.DateTimeField(null=True,blank=True)
#     inspection_date_end = models.DateTimeField(null=True, blank=True)
#     accepted_no = models.IntegerField(null=True)
#     accepted_with_deviation_no = models.IntegerField(null=True)
#     rework_no = models.IntegerField(null=True)
#     rejection_mat_no = models.IntegerField(null=True)
#     rejection_job_no = models.IntegerField(null=True)
#     completed = models.BooleanField(default=False)
#     double_sampling = models.BooleanField(default=False)
#     double_sampling_exists = models.BooleanField(default=False)
#     double_sampling_rows = models.IntegerField(null=True,blank=True)
#     grn_gen = models.BooleanField(default=False)
#     hold = models.BooleanField(default=False)
#     # debit_note_rised_job = models.BooleanField(default=False)
#     # debit_note_no_job = models.IntegerField(null=True, blank=True)
#     # debit_note_rised_mat = models.BooleanField(default=False)
#     # debit_note_no_mat = models.CharField(null=True,blank=True,max_length=1024)
#     raw_mat_cmp_reff = models.BooleanField(default=False)
#     rework_rised = models.BooleanField(default=False)
#     rework_dc_no = models.IntegerField(null=True, blank=True)
#     inspecreport =  models.IntegerField(null=True,blank=True)
#     testreport = models.BooleanField(default=False)
#     financial_year = models.DateField(auto_now=True)
#     worker_name=models.CharField(max_length=1024)

#     objects = YEAR_MANAGER()
#     def __str__(self):
#         return str(self.report_no) + '  -  ' + str(self.double_sampling)

# class joborder_inspection_remarks_relation(models.Model):
#     inspection_report_details_joborder = models.ForeignKey(inspection_report_details_joborder, null=True, blank=True, on_delete=models.CASCADE)
#     qc_remarks_list = models.ForeignKey(qc_remarks_list, null=True, blank=True, on_delete=models.CASCADE)
#     material = models.BooleanField(default=False)
#     rework = models.BooleanField(default=False)
#     job = models.BooleanField(default=False)
#     financial_year = models.DateField(auto_now=True)

#     objects = YEAR_MANAGER()
#     def __str__(self):
#         return str(self.inspection_report_details_joborder) + '  -  ' + str(self.qc_remarks_list) + ' - ' + str(self.id)
