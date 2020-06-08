# Generated by Django 3.0.6 on 2020-06-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Histr',
            fields=[
                ('isin', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='sStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=500)),
                ('nct', models.CharField(max_length=500)),
                ('completion_date', models.DateField(auto_now=True)),
                ('phase', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=255)),
                ('conditions', models.CharField(max_length=255)),
                ('interventions', models.CharField(max_length=255)),
                ('market_cap', models.FloatField()),
                ('net_Cash', models.FloatField()),
                ('epv', models.FloatField()),
                ('downside', models.FloatField()),
                ('Upside', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('isin', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
        ),
    ]
