# Generated by Django 4.1.3 on 2022-12-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0007_remove_towers_tools_tower_towers_tools_tower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='towersandtools',
            name='id_tool',
        ),
        migrations.RemoveField(
            model_name='towersandtools',
            name='id_towers',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='tools_customer',
        ),
        migrations.DeleteModel(
            name='CustomersAndTools',
        ),
        migrations.DeleteModel(
            name='TowersAndTools',
        ),
        migrations.AddField(
            model_name='customers',
            name='tools_customer',
            field=models.ManyToManyField(to='sections.tools'),
        ),
    ]