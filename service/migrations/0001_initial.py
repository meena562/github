# Generated by Django 3.0 on 2021-04-24 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(choices=[('su', 'suziki'), ('b', 'BMW'), ('TO', 'Toyota')], max_length=100)),
                ('carno', models.TextField(max_length=20)),
                ('service_type', models.CharField(choices=[('w', 'waterwash'), ('T', 'typechange'), ('F', 'fullservice')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('da', models.DateField(auto_now_add=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
