# Generated by Django 3.0.5 on 2020-05-12 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('users', '0003_delete_recentlyviewedanonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentlyviewed',
            name='productID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Product'),
        ),
    ]
