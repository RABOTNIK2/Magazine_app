# Generated by Django 5.0.6 on 2024-05-14 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proect', '0003_alter_order_owner_alter_order_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='products', to='proect.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='cart',
            field=models.ManyToManyField(blank=True, to='proect.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to='proect.user'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
