# Generated by Django 3.1.7 on 2022-06-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('expense_name', models.CharField(max_length=254, verbose_name='اسم المصروف')),
                ('qty', models.PositiveSmallIntegerField(verbose_name='الكمية')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='السعر')),
                ('notes', models.CharField(blank=True, max_length=254, null=True, verbose_name='ملاحظات')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('item_name', models.CharField(max_length=254, verbose_name='اسم المنتج')),
                ('qty', models.PositiveSmallIntegerField(verbose_name='الكمية')),
                ('wholesale_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=' سعر بيع الجمله')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('day', models.CharField(blank=True, max_length=200, null=True)),
                ('item_name', models.CharField(max_length=254, verbose_name='اسم المنتج')),
                ('qty', models.PositiveSmallIntegerField(verbose_name='الكمية')),
                ('Purchase_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر الشراء')),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر البيع')),
                ('wholesale_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name=' سعر بيع الجمله')),
                ('notes', models.CharField(blank=True, max_length=254, null=True, verbose_name='ملاحظات')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('day', models.CharField(blank=True, max_length=200, null=True)),
                ('item_name', models.CharField(max_length=254, verbose_name='اسم المنتج')),
                ('qty', models.PositiveSmallIntegerField(verbose_name='الكمية')),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر البيع')),
                ('notes', models.CharField(blank=True, max_length=254, null=True, verbose_name='ملاحظات')),
            ],
        ),
    ]
