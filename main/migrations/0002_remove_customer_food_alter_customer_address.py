# Generated by Django 4.2.4 on 2023-09-05 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='food',
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=50),
        ),
    ]
