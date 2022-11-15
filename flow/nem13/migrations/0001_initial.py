# Generated by Django 4.1.3 on 2022-11-13 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccumulationMeterData',
            fields=[
                ('record_indicator', models.IntegerField(max_length=3)),
                ('nmi', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('nmi_configuration', models.CharField(max_length=240)),
                ('register_id', models.CharField(max_length=10)),
                ('nmi_suffix', models.CharField(max_length=2)),
                ('mdm_data_stream_identifier', models.CharField(blank=True, max_length=2)),
                ('meter_serial_number', models.CharField(max_length=12)),
                ('direction_indicator', models.CharField(max_length=1)),
                ('previous_register_read', models.CharField(max_length=15)),
                ('previous_register_read_date_time', models.DateTimeField(max_length=14)),
                ('previous_quality_method', models.CharField(max_length=3)),
                ('previous_reason_code', models.IntegerField(blank=True, max_length=3)),
                ('previous_reason_description', models.CharField(blank=True, max_length=240)),
                ('current_register_read', models.CharField(max_length=15)),
                ('current_register_read_date_time', models.DateTimeField(max_length=14)),
                ('current_quality_method', models.CharField(max_length=3)),
                ('current_reason_code', models.IntegerField(blank=True, max_length=3)),
                ('current_reason_description', models.CharField(blank=True, max_length=240)),
                ('quantity', models.CharField(max_length=5)),
                ('uom', models.CharField(max_length=5)),
                ('next_scheduled_read_date', models.DateField(blank=True, max_length=8)),
                ('update_date_time', models.DateTimeField(max_length=14)),
                ('msa_ts_load_date_time', models.DateTimeField(max_length=14)),
                ('file_path', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='B2BDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_indicator', models.IntegerField(max_length=3)),
                ('previous_trans_code', models.CharField(max_length=1)),
                ('previous_ret_service_order', models.CharField(max_length=15)),
                ('current_trans_code', models.CharField(max_length=1)),
                ('current_ret_service_order', models.CharField(max_length=15)),
                ('file_path', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='End',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_indicator', models.IntegerField(max_length=3)),
                ('file_path', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_indicator', models.IntegerField(max_length=3)),
                ('version_header', models.CharField(max_length=5)),
                ('date_time', models.DateTimeField()),
                ('from_participant', models.CharField(max_length=10)),
                ('to_participant', models.CharField(max_length=10)),
                ('file_path', models.FilePathField()),
            ],
        ),
    ]
