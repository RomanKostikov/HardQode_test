# Generated by Django 5.0.2 on 2024-03-01 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='lessons_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]