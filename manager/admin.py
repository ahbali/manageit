from manager.models import Equipment, SSLCert, Software, Person, SupportContract
from django.contrib import admin


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "equipment_type",
        "ip",
        "fqdn",
        "license_end",
        "environment",
    )
    list_filter = ("license_end", "environment")


@admin.register(SSLCert)
class SSLCertAdmin(admin.ModelAdmin):
    list_display = ("name", "expiration_date")
    list_filter = ("expiration_date",)


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ("name", "equipment", "environment")
    list_filter = ("environment", "ship_to_prod_date")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "phone_number")


@admin.register(SupportContract)
class SupportContractAdmin(admin.ModelAdmin):
    list_display = ("support_provider", "contract_date", "expiration_date")
    list_filter = ("expiration_date", "contract_date")


# Register your models here.
admin.AdminSite.site_header = "ManageIt Administration"
# admin.site.register(Equipment)
# admin.site.register(Software)
# admin.site.register(Person)
# admin.site.register(SupportContract)
# admin.site.register(SSLCert)
