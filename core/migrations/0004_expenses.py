# Generated by Django 3.1.7 on 2021-04-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210305_2145'),
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
    ]
