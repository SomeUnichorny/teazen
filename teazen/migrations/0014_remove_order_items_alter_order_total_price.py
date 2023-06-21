# Generated by Django 4.1.7 on 2023-04-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teazen', '0013_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
