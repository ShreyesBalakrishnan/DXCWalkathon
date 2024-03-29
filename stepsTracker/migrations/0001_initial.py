# Generated by Django 3.1.5 on 2021-01-08 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('steps', models.IntegerField(default=0)),
                ('week1', models.IntegerField()),
                ('week2', models.IntegerField()),
                ('week3', models.IntegerField()),
                ('week4', models.IntegerField()),
                ('week5', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
