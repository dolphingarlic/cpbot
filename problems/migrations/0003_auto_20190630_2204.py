# Generated by Django 2.2.2 on 2019-07-01 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_auto_20190630_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='problem',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='source',
            name='abbreviation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
