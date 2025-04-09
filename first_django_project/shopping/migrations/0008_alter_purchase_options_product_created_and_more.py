# Generated by Django 5.1.7 on 2025-04-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_alter_customeraddress_country_purchase_purchaseitem_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['purchase_date']},
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
