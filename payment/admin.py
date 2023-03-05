from django.contrib import admin

from .models import Payment, PaymentDetails


# Register your models here.


class PaymentItemsInline(admin.TabularInline):
    model = PaymentDetails
    row_id_field = ["payment"]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["merchant_request_id", "checkout_request_id", "result_code", "result_description"]
    list_filter = ["result_code", "result_description"]
    inlines = [PaymentItemsInline]
