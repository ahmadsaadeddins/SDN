# Generated by Django 4.1.3 on 2022-12-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0009_towers_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='ip_tool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tools',
            name='mac_tool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tools',
            name='model_tool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tools',
            name='name_tool',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tools',
            name='ssid_tool',
            field=models.CharField(max_length=100, null=True),
        ),
    ]