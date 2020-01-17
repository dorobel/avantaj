# Generated by Django 2.2.5 on 2020-01-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('loan_nbr', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=2)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('close_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
