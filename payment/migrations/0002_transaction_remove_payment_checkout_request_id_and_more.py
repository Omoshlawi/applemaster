# Generated by Django 4.0.8 on 2023-03-05 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_paymentdetails_payment_delete_payment_and_more'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_request_id', models.CharField(max_length=100)),
                ('checkout_request_id', models.CharField(max_length=100)),
                ('result_code', models.IntegerField()),
                ('result_description', models.TextField()),
                ('mpesa_receipt_number', models.CharField(blank=True, max_length=100, null=True)),
                ('transaction_date', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='checkout_request_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='merchant_request_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='result_code',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='result_description',
        ),
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='orders.order'),
        ),
        migrations.DeleteModel(
            name='PaymentDetails',
        ),
        migrations.AddField(
            model_name='transaction',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='payment.payment'),
        ),
    ]
