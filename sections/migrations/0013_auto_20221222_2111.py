# Generated by Django 3.1.7 on 2022-12-22 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0012_auto_20221222_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='towers',
            name='tools_tower',
        ),
        migrations.AddField(
            model_name='towers',
            name='tools_tower',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sections.tools'),
            preserve_default=False,
        ),
    ]
