# Generated by Django 2.2.10 on 2020-06-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('L', 'Lenovo'), ('D', 'Dell'), ('A', 'Acer')], max_length=2),
        ),
    ]
