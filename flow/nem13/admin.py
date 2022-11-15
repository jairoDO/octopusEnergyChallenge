from django.contrib import admin
from .models import Header, AccumulationMeterData, B2BDetails


# Register your models here.
class AccumulationMeterDataAdmin(admin.ModelAdmin):
    search_fields = ['nmi', 'meter_serial_number']

admin.site.register(AccumulationMeterData, AccumulationMeterDataAdmin)
admin.site.register(B2BDetails)
admin.site.register(Header)


