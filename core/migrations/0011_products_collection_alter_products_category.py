# Generated by Django 4.1.4 on 2022-12-30 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.collection'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
        ),
    ]