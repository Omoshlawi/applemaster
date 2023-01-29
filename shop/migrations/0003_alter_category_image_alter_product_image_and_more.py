# Generated by Django 4.0.8 on 2023-01-03 06:47

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_image_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.category_file_name),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=shop.models.product_file_name),
        ),
        migrations.AlterField(
            model_name='productsecondaryimages',
            name='image',
            field=models.ImageField(upload_to=shop.models.product_secondary_image_name),
        ),
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ImageField(upload_to=shop.models.tag_file_name),
        ),
    ]
