# Generated by Django 5.0.2 on 2024-02-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_cost_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
