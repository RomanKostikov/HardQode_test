# Generated by Django 5.0.2 on 2024-02-29 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_group_current_users_remove_group_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='student_count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(150)]),
        ),
    ]
