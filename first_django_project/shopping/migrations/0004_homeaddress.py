# Generated by Django 5.1.7 on 2025-04-02 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_product_expiry_dte_product_is_discounted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('house_number', models.CharField(max_length=4)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='shopping.customer')),
            ],
        ),
    ]
