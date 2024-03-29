# Generated by Django 3.2.2 on 2021-05-07 10:47

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepsTracker', '0004_auto_20210117_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='week5',
        ),
        migrations.AlterField(
            model_name='step',
            name='steps',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='step',
            name='week1',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='step',
            name='week2',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='step',
            name='week3',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='step',
            name='week4',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
