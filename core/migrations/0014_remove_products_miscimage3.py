# Generated by Django 4.1.4 on 2023-01-01 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_products_miscimage1_products_miscimage2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='miscImage3',
        ),
    ]
