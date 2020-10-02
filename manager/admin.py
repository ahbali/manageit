from manager.models import Equipment, SSLCert, Software, Person, SupportContract
from django.contrib import admin

# Register your models here.
admin.AdminSite.site_header = "ManageIt Administration"
admin.site.register(Equipment)
admin.site.register(Software)
admin.site.register(Person)
admin.site.register(SupportContract)
admin.site.register(SSLCert)
