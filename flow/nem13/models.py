from django.db import models

class Header(models.Model):
    file_path = models.CharField(max_length=240, name='file_path')
    record_indicator = models.IntegerField()
    version_header = models.CharField(max_length=5)
    date_time = models.DateTimeField(name='date_time')
    from_participant = models.CharField(max_length=10)
    to_participant = models.CharField(max_length=10)
    file_path = models.FilePathField()

    class Meta:
        unique_together = ['file_path', 'date_time']

    def __str__(self):
        return f'Header from_participant:{self.from_participant} datetime {self.date_time}'

class AccumulationMeterData(models.Model):
    record_indicator = models.IntegerField()
    nmi = models.IntegerField()
    nmi_configuration = models.CharField(max_length=240)
    register_id = models.CharField(max_length=10)
    nmi_suffix = models.CharField(max_length=2)
    mdm_data_stream_identifier = models.CharField(max_length=2, blank=True)
    meter_serial_number = models.CharField(max_length=12)
    direction_indicator = models.CharField(max_length=1)
    previous_register_read = models.CharField(max_length=15)
    previous_register_read_date_time = models.DateTimeField(max_length=14)
    previous_quality_method = models.CharField(max_length=3)
    previous_reason_code = models.IntegerField(blank=True, null=True)
    previous_reason_description = models.CharField(max_length=240, blank=True)
    current_register_read = models.CharField(max_length=15)
    current_register_read_date_time = models.DateTimeField(max_length=14)
    current_quality_method = models.CharField(max_length=3)
    current_reason_code = models.IntegerField(blank=True)
    current_reason_description = models.CharField(max_length=240, blank=True)
    quantity = models.CharField(max_length=5)
    uom = models.CharField(max_length=5)
    next_scheduled_read_date = models.DateField(max_length=8, blank=True)
    update_date_time = models.DateTimeField(max_length=14)
    msa_ts_load_date_time = models.DateTimeField(max_length=14)
    file_path = models.CharField(max_length=240)

    class Meta:
        unique_together = ['file_path', 'nmi', 'meter_serial_number', 'msa_ts_load_date_time']

    def __str__(self):
        return f'Accumulation Meter Data nmi:{self.nmi}, meter_data_serial: {self.meter_serial_number}'

class B2BDetails(models.Model):
    record_indicator = models.IntegerField()
    previous_trans_code = models.CharField(max_length=1)
    previous_ret_service_order = models.CharField(max_length=15)
    current_trans_code = models.CharField(max_length=1, blank=True)
    current_ret_service_order = models.CharField(max_length=15, blank=True)
    file_path = models.CharField(max_length=240)


    class Meta:
        unique_together = ['file_path', 'previous_ret_service_order', 'current_ret_service_order']

    def __str__(self):
        return f'B2B Details {self.file_path}'


class End(models.Model):
    file_path = models.CharField(max_length=240)
    record_indicator = models.IntegerField()


