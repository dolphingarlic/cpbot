# Generated by Django 2.2.2 on 2019-07-02 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abbreviation', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('abbreviation', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(default='https://oj.uz/')),
                ('from_year', models.IntegerField(default=2002)),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='problems.Source')),
            ],
        ),
    ]
