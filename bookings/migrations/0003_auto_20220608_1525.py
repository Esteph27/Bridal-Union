# Generated by Django 3.2 on 2022-06-08 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20220608_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_wedding',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='booking',
            name='select_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
