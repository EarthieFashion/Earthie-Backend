# Generated by Django 4.1.4 on 2022-12-28 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_homeblockoffers_dateuploaded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=255)),
                ('dateCreated', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='offerslider',
            name='dateUploaded',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productSKU', models.CharField(max_length=255)),
                ('prodcutName', models.CharField(max_length=255)),
                ('productPrice', models.CharField(max_length=255)),
                ('stock', models.CharField(max_length=255)),
                ('productImage', models.ImageField(upload_to='images/products/')),
                ('is_published', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
    ]
