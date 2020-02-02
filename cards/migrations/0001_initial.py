# Generated by Django 3.0.2 on 2020-02-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=2)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
