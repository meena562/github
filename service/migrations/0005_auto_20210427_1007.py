# Generated by Django 3.0 on 2021-04-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_userservice_carno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userservice',
            name='car_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userservice',
            name='service_type',
            field=models.CharField(max_length=100),
        ),
    ]