# Generated by Django 5.0 on 2024-01-28 14:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi', '0003_posting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
