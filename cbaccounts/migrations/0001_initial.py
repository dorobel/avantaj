# Generated by Django 2.2.5 on 2020-01-15 16:53

from django.db import migrations, models
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acct_nbr', encrypted_model_fields.fields.EncryptedCharField()),
                ('balance', models.IntegerField()),
                ('acct_type', models.CharField(max_length=2)),
            ],
        ),
    ]
