# Generated by Django 4.1.3 on 2022-11-14 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nem13', '0008_alter_b2bdetails_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accumulationmeterdata',
            unique_together={('file_path', 'nmi', 'meter_serial_number', 'msa_ts_load_date_time')},
        ),
    ]
