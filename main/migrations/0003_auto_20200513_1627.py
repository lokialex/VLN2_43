# Generated by Django 3.0.5 on 2020-05-13 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='onSale',
            new_name='on_sale',
        ),
    ]
