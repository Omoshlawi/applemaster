from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order


# Create your models here.


class Payment(models.Model):
    order = models.ForeignKey(Order, related_name="payment", on_delete=models.CASCADE)
    merchant_request_id = models.CharField(max_length=100)
    checkout_request_id = models.CharField(max_length=100)
    result_code = models.IntegerField()
    result_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order}'s Payment"


class PaymentDetails(models.Model):
    payment = models.OneToOneField(Payment, related_name='items', on_delete=models.CASCADE)
    mpesa_receipt_number = models.CharField(max_length=100, null=True, blank=True)
    transaction_date = models.CharField(max_length=256, null=True, blank=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2)


@receiver(post_save, sender=PaymentDetails)
def check_if_payment_complete_and_mark_paid(sender, instance, created, **kwargs):
    if created:
        # update order payment status to true if balance is o
        _order = instance.payment.order
        if _order.get_balance() <= 0.95:
            _order.paid = True
            _order.save()
        else:
            _order.paid = False
            _order.save()
