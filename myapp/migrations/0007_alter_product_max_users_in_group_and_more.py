# Generated by Django 5.0.2 on 2024-02-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_creator_alter_product_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='max_users_in_group',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='min_users_in_group',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
