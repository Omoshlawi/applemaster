# Generated by Django 4.0.8 on 2022-12-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_alter_contactinfo_logo_alter_frontdisplay_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='about_us',
            field=models.TextField(blank=True, null=True),
        ),
    ]
