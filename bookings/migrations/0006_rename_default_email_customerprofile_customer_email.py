# Generated by Django 3.2 on 2022-06-10 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20220610_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerprofile',
            old_name='default_email',
            new_name='customer_email',
        ),
    ]