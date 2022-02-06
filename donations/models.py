
from posts.models import Donner

from django.db import models

class Basetable(models.Model):
    user = models.ForeignKey(Donner, on_delete=models.CASCADE)
    basetable_id = models.AutoField(primary_key=True)
    notes = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.IntegerField()
    amount_refunded = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    error_reason = models.CharField(max_length=100)
    error_description = models.CharField(max_length=100)
    captured = models.BooleanField()
    contact = models.CharField(max_length=100)
    invoice_id = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    international = models.BooleanField()
    email = models.CharField(max_length=100)
    amount = models.IntegerField()
    refund_status = models.CharField(max_length=100)
    wallet = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    vpa = models.CharField(max_length=100)
    error_source = models.CharField(max_length=100)
    error_step = models.CharField(max_length=100)
    tax = models.CharField(max_length=100)
    card_id = models.CharField(max_length=100)
    error_code = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    entity = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    

class Acquirer_data(models.Model):
    acquirer_data_id = models.AutoField(primary_key=True)
    rrn = models.CharField(max_length=100)
    basetable_id = models.OneToOneField(Basetable,on_delete=models.CASCADE)
class Donner_paydetails(models.Model):
    # user = models.ForeignKey(Donner, on_delete=models.CASCADE)
    ngo_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now=True)
    rez_payment_id=models.CharField(max_length=100,blank=True)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        return self. ngo_name
    



