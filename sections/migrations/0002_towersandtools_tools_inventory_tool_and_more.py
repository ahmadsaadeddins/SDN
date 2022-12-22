# Generated by Django 4.1.3 on 2022-12-20 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TowersAndTools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tool', models.IntegerField()),
                ('id_towers', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='tools',
            name='inventory_tool',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sections.inventory'),
        ),
        migrations.AddField(
            model_name='towers',
            name='tools_tower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sections.towersandtools'),
        ),
    ]