# Generated by Django 4.0.8 on 2023-02-28 06:15

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import root.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('about_us', models.TextField(blank=True, null=True)),
                ('street', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('twitter_handle', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('linked_in', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to=root.models.logo_filename)),
            ],
        ),
        migrations.CreateModel(
            name='FrontDisplayCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('Sliders', 'Sliders'), ('Brands', 'Brands')], db_index=True, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubSubscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_subscribed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='FrontDisplay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=root.models.content_file_name)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='displays', to='root.frontdisplaycategory')),
            ],
        ),
    ]
