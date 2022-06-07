# Generated by Django 3.2 on 2022-06-06 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_marketplace', '0006_alter_imagecomments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecomments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]