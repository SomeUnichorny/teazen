# Generated by Django 4.1.7 on 2023-04-04 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teazen', '0020_alter_orderitem_options_order_items_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
    ]