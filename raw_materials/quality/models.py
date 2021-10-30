from django.db import models
import datetime

# Create your models here.

class finacialyear(models.QuerySet):
    def finpd(self):
        year = datetime.time.now().year
        startyear = datetime.datetime(year, 4, 1)
        endyear = datetime.datetime(year, 31, 3)
        return self.filter(finperiod_gte=startyear, finperiod_lte=endyear)


def reportnumber():
    lastreportnumber = inspection_report_details.objects.all().order_by('id').last()
    if not lastreportnumber :
        return 'RE0001'
    report_no = lastreportnumber .report_no
    report_no_int = int(report_no.split('CASE')[-1])
    print(report_no )
    newreportno_int=report_no_int +1
    newreportno = 'RE' + str(newreportno_int)
    return newreportno

st=[(1,'OK'),(2,'REJECTED')]

class inspection_report_details(models.Model):
    report_no = models.CharField(max_length=45,null=True,default=reportnumber)
    inspection_date_start = models.DateTimeField(null=True, blank=True)
    inspection_date_end = models.DateTimeField(null=True, blank=True)
    sample_size=models.FloatField(null=True)
    accepted_no = models.FloatField(null=True)
    accepted_with_deviation_no = models.FloatField(null=True)
    rejection_no = models.FloatField(null=True)
    test_report = models.BooleanField(default=False)
    status = models.BooleanField(null=True, blank=True)
    statusreport=models.CharField(max_length=100,choices=st,null=True, blank=True)
    finacial_year = models.DateField(auto_now=True)
    objects = finacialyear()
    raw_component=models.PositiveIntegerField()
    def __str__(self):
        return self.report_no


class parameters(models.Model):

    field1= models.FloatField(null=True)
    field2 = models.FloatField(null=True)
    field3 = models.FloatField(null=True)
    field4 = models.FloatField(null=True)
    field5 = models.FloatField(null=True)


    def __str__(self):
        return self.field1


sta=[(1,'ok'),(2,'not ok'),(3,'tested partially')]
class inspection_report_rows(models.Model):

    inspection_report = models.ForeignKey(inspection_report_details, null=True, blank=True, on_delete=models.CASCADE)
    no_of_sample = models.IntegerField(null=True)
    smp_no = models.IntegerField(null=True)
    parameter_required = models.CharField(max_length=30,null=True)
    val= models.FloatField(null=True)
    statusreport = models.CharField(max_length=100, choices=sta, null=True, blank=True)

    def __str__(self):
        return str(self.smp_no)


remark_list=[(1,'list1'),(2,'list2'),(3,'list3'),(4,'list4'),(5,'list5')]
class remarks(models.Model):
    inspection_report = models.ForeignKey(inspection_report_details, null=True, blank=True, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=50, choices=remark_list, default=1)

