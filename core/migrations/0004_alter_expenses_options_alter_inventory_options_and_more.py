# Generated by Django 4.0.5 on 2022-06-15 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_inventory_item_name_alter_purchase_item_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expenses',
            options={'verbose_name': 'المصاريف', 'verbose_name_plural': 'المصاريف'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'المخزن', 'verbose_name_plural': 'المخزن'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'المشتريات', 'verbose_name_plural': 'المشتريات'},
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name': 'المبيعات', 'verbose_name_plural': 'المبيعات'},
        ),
    ]
