# Generated by Django 4.0.8 on 2023-03-05 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_paymentdetails_payment_delete_payment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
    ]