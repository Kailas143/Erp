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
    lastreportnumber = inspection_report_details_raw_materials.objects.all().order_by('id').last()
    if not lastreportnumber :
        return 'RE0001'
    report_no = lastreportnumber.report_no
    report_no_int = int(report_no.split('E')[-1])
    
  
    newreportno_int=report_no_int +1
    newreportno = 'RE000' + str(newreportno_int)
    return newreportno

st=[(1,'OK'),(2,'REJECTED')]

class inspection_report_details_raw_materials(models.Model):
    tenant_id=models.PositiveIntegerField()
    raw_material_fin_material_bill_inward =PositiveIntegerField(null=True)
    raw_material_fin_material_dc_inward =PositiveIntegerField(null=True)
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

class inspection_report_rows_raw_materials(models.Model):
    tenant_id=models.PositiveIntegerField()
    inspection_report = models.ForeignKey(inspection_report_details_raw_materials, null=True, blank=True, on_delete=models.CASCADE)
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
    inspection_report = models.ForeignKey(inspection_report_details_raw_materials, null=True, blank=True, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=50, choices=remark_list, default=1)
    worker_name=models.CharField(max_length=1024)
    financial_year = models.DateField(auto_now=True)
    objects = finacialyear()

