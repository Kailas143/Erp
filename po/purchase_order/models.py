from django.db import models
import datetime
# Create your models here.
class FinancialQuerySet(models.QuerySet):
    def current_financialyear(self):
        year = datetime.datetime.now().year
        current_finyear_start= datetime.datetime(year, 4, 1)#current_finyear_start 2021
        current_finyear_end= datetime.datetime(year+1, 3, 31)#current_finyear_end 2022
        return self.filter(financial_period__gte=current_finyear_start,financial_period__lte=current_finyear_end,tenant_id='1')

class po_details(models.Model):
    tenant_id=models.PositiveIntegerField()
    supliers_details =  models.PositiveIntegerField()
    po_no =  models.IntegerField(null=True)
    date = models.DateField(null=True)
    mail_date = models.DateField(null=True)
    bill_amt=models.FloatField(null=True)
    t_amount = models.FloatField(null=True)
    t_gst=models.FloatField(null=True)
    igst_amount=models.FloatField(null=True)
    sgst_amount = models.FloatField(null=True)
    cgst_amount = models.FloatField(null=True)
    draft=models.BooleanField(default=True)
    gm_aprove = models.IntegerField(null=True,blank=True)
    pro_aprove = models.IntegerField(null=True,blank=True)
    admin_aprove = models.IntegerField(null=True,blank=True)
    admin_check = models.BooleanField(default=False)
    not_sent = models.BooleanField(default=True)
    cancel=models.BooleanField(default=False)
    send_status = models.IntegerField(null=True,blank=True)
    recive_status = models.IntegerField(null=True, blank=True)
    financial_year = models.DateField(auto_now=True)
    # objects=models.Manager()
    # period=FinancialQuerySet.as_manager()

    objects = FinancialQuerySet.as_manager()
    def __str__(self):
        return str(self.po_no) + '  -  ' + str(self.id) + '  -  ' + str(self.date)

class po_request_response(models.Model):
    tenant_id=models.PositiveIntegerField()
    po_details = models.ForeignKey(po_details, null=True, db_column='po_no', blank=True, on_delete=models.CASCADE)
    role = models.CharField(null=True,blank=True, max_length=1024)
    date_time = models.DateTimeField(null=True)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()


    def __str__(self):
        return str(self.po_details) + '  -  ' + str(self.role)+ '  -  ' + str(self.date_time)+ '  -  ' + str(self.accepted)

class po_no_increment(models.Model):
    tenant_id=models.PositiveIntegerField()
    po_no = models.IntegerField(null=True)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()

    
    def __str__(self):
        return str(self.po_no) + '  -  ' + str(self.id)

class po_order_list(models.Model):
    tenant_id=models.PositiveIntegerField()
    po_details = models.ForeignKey(po_details, blank=True, null=True, on_delete=models.CASCADE)
    raw_components_price = models.PositiveIntegerField()
    qty = models.IntegerField(null=True)
    bal_qty = models.IntegerField(null=True)
    bill_amt = models.FloatField(null=True)
    igst_amount=models.FloatField(null=True)
    sgst_amount = models.FloatField(null=True)
    cgst_amount = models.FloatField(null=True)
    tgst=models.FloatField(null=True)
    t_amount=models.FloatField(null=True)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()


    def __str__(self):
        return str(self.po_details.po_no) + '  -  ' + str(self.qty)+ '  -  ' + str(self.bal_qty)+ '  -  ' + str(self.id)

class order_schelude_list(models.Model):
    tenant_id=models.PositiveIntegerField()
    po_order_list = models.ForeignKey(po_order_list, null=True, db_column='order', blank=True, on_delete=models.CASCADE)
    delivery_date = models.DateField(null=True)
    qty = models.IntegerField(null=True)
    bal_qty = models.IntegerField(null=True)
    table_no=models.BooleanField(default=False)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()


    def __str__(self):
        return str(self.po_order_list) + '  -  ' + str(self.delivery_date)


class mail_sent_details(models.Model):
    tenant_id=models.PositiveIntegerField()
    recivers_details =  models.PositiveIntegerField()
    email_user_id=models.EmailField(null=True,blank=True)
    mail_id = models.CharField(null=True,blank=True, max_length=1024)
    mail_subject = models.CharField(null=True,blank=True, max_length=1024)
    po_details= models.ForeignKey(po_details, null=True, blank=True, on_delete=models.CASCADE)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()


    def __str__(self):
        return str(self.recivers_details) + '  -  ' + str(self.mail_id)+ '  -  ' + str(self.mail_subject)

class mail_recived_details(models.Model):
    tenant_id=models.PositiveIntegerField()
    sender_details =  models.PositiveIntegerField()
    email_user_id = models.EmailField(null=True, blank=True)
    mail_id = models.CharField(null=True,blank=True, max_length=1024)
    mail_subject = models.CharField(null=True,blank=True, max_length=1024)
    date_time=models.DateTimeField(null=True)
    mail_discuss = models.BooleanField(default=False)
    auto_reff=models.BooleanField(default=False)
    uncat=models.BooleanField(default=False)
    po_refff = models.BooleanField(default=False)
    rate_refff = models.BooleanField(default=False)
    unwanted = models.BooleanField(default=False)
    reffrenece_user = models.CharField(null=True,max_length=102)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()


    def __str__(self):
        return str(self.sender_details) + '  -  ' + str(self.mail_id)+ '  -  ' + str(self.mail_subject)

class recived_mail_po_reff(models.Model):
    tenant_id=models.PositiveIntegerField()
    po_details = models.ForeignKey(po_details, null=True, blank=True, on_delete=models.CASCADE)
    mail_recived_details= models.ForeignKey(mail_recived_details, null=True, blank=True, on_delete=models.CASCADE)
    stauts = models.BooleanField(default=False)
    mail_sent_details= models.ForeignKey(mail_sent_details, null=True, blank=True, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    resons = models.CharField(null=True,blank=True,max_length=1024)
    withoutmail = models.BooleanField(default=False)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()

    
    def __str__(self):
        return str(self.mail_recived_details) + '  -  ' + str(self.po_details)

class  price_update_request(models.Model):
    tenant_id=models.PositiveIntegerField()
    mail_recived_details = models.ForeignKey(mail_recived_details, null=True, blank=True,on_delete=models.CASCADE)
    company_details =   models.PositiveIntegerField()
    raw_components_price = models.PositiveIntegerField()
    quote_val = models.FloatField(null=True)
    action = models.BooleanField(null=True)
    admin_quote_val= models.FloatField(null=True)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()

  
    def __str__(self):
        return str(self.mail_recived_details) + '  -  ' + str(self.company_details) + '  -  ' + str(
            self.raw_components_price) + '  -  ' + str(self.quote_val)

class excess_po_verification(models.Model):
    tenant_id=models.PositiveIntegerField()
    raw_components_details = models.PositiveIntegerField()
    store_min=models.IntegerField(null=True)
    store_max=models.IntegerField(null=True)
    store_bal=models.IntegerField(null=True)
    po_bal=models.IntegerField(null=True)
    draft_bal=models.IntegerField(null=True)
    reson=models.TextField(null=True,blank=True)
    permission=models.BooleanField(default=False)
    date_time=models.DateTimeField(null=True)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()


    def __str__(self):
        return str(self.date_time) + '  -  ' +str(self.raw_components_details) + '  -  ' + str(self.reson) + '  -  ' + str(self.permission)

class mail_sent_details_po_cancel(models.Model):
    tenant_id=models.PositiveIntegerField()
    recivers_details =  models.PositiveIntegerField()
    email_user_id=models.EmailField(null=True,blank=True)
    mail_id = models.CharField(null=True,blank=True, max_length=1024)
    mail_subject = models.CharField(null=True,blank=True, max_length=1024)
    po_details = models.ForeignKey(po_details, null=True, blank=True, on_delete=models.CASCADE)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()

    def __str__(self):
        return str(self.recivers_details) + '  -  ' + str(self.mail_id)+ '  -  ' + str(self.mail_subject)

class mail_recived_details_po_cancel(models.Model):
    tenant_id=models.PositiveIntegerField()
    sender_details =  models.PositiveIntegerField()
    email_user_id = models.EmailField(null=True, blank=True)
    mail_id = models.CharField(null=True,blank=True, max_length=1024)
    mail_subject = models.CharField(null=True,blank=True, max_length=1024)
    date_time=models.DateTimeField(null=True)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()

    
    def __str__(self):
        return str(self.sender_details) + '  -  ' + str(self.mail_id)+ '  -  ' + str(self.mail_subject)

class recived_mail_po_reff_cancel(models.Model):
    tenant_id=models.PositiveIntegerField()
    po_details = models.ForeignKey(po_details, null=True, blank=True, on_delete=models.CASCADE)
    mail_recived_details_po_cancel= models.ForeignKey(mail_recived_details_po_cancel, null=True, blank=True, on_delete=models.CASCADE)
    mail_sent_details_po_cancel= models.ForeignKey(mail_sent_details_po_cancel, null=True, blank=True, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()

   
    def __str__(self):
        return str(self.mail_recived_details_po_cancel) + '  -  ' + str(self.po_details)

class raw_material_error_to_error_tally(models.Model):
    tenant_id=models.PositiveIntegerField()
    raw_inward_for = models.IntegerField(null=True)
    raw_inward_used = models.IntegerField(null=True)
    for_qty_in = models.IntegerField(null=True)
    for_qty_left = models.IntegerField(null=True)
    used_qty_in = models.IntegerField(null=True)
    used_qty_left = models.IntegerField(null=True)
    financial_year = models.DateField(auto_now=True)
    objects = FinancialQuerySet.as_manager()

  
    def __str__(self):
        return str(self.raw_inward_for) + '  -  ' + str(self.raw_inward_used)