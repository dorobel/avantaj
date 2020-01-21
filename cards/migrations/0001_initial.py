# Generated by Django 2.2.5 on 2020-01-21 19:36

from django.db import migrations, models
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_nbr', encrypted_model_fields.fields.EncryptedCharField()),
                ('cvv_code', encrypted_model_fields.fields.EncryptedCharField()),
                ('card_type', models.CharField(max_length=2)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
