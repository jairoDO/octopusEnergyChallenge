# Generated by Django 4.1.3 on 2022-11-14 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nem13', '0007_remove_accumulationmeterdata_nem13_accum_file_pa_dc30b6_idx'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='b2bdetails',
            unique_together={('file_path', 'previous_ret_service_order', 'current_ret_service_order')},
        ),
        migrations.AlterUniqueTogether(
            name='header',
            unique_together={('file_path', 'date_time')},
        ),
    ]
