# Generated by Django 4.1.4 on 2023-01-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_products_is_in_offer_products_offerby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='miscImage1',
            field=models.ImageField(blank=True, default='media/images/products/Screenshot_2023-01-01_105220.png', null=True, upload_to='images/products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='miscImage2',
            field=models.ImageField(blank=True, default='media/images/products/Screenshot_2023-01-01_105220.png', null=True, upload_to='images/products/'),
        ),
    ]