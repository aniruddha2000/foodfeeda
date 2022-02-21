from django.db import models


class DonnerPayDetails(models.Model):
    # donation_maker = models.ForeignKey(Donner, on_delete=models.CASCADE, null=True)
    donner_id = models.BigIntegerField(default=1)
    ngo_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now=True)
    rez_payment_id = models.CharField(max_length=100, blank=True)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        return self.ngo_name
