# Generated by Django 5.0.6 on 2024-06-26 13:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proect', '0009_alter_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
