# Generated by Django 3.1.5 on 2021-01-08 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stepsTracker', '0002_auto_20210108_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='week1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='week2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='week3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='week4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='week5',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
