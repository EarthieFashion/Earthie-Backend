# Generated by Django 4.1.4 on 2022-12-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_category_alter_offerslider_dateuploaded_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='dateAdded',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]