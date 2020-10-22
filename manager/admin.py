from datetime import datetime
from typing import Any
from manager.forms import (
    EquipmentMultipleDocumentationForm,
    SoftwareMultipleDocumentationForm,
)
from manager.models import (
    EquipmentDocumentation,
    DocumentationMany,
    SoftwareDocumentation,
    Equipment,
    SSLCert,
    Software,
    Person,
    SupportContract,
)
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class EquipmentDocumentationInline(admin.StackedInline):
    model = EquipmentDocumentation
    extra = 0


class SoftwareDocumentationInline(admin.StackedInline):
    model = SoftwareDocumentation
    extra = 0


class EquipmentInline(admin.TabularInline):
    model = Equipment
    fields = (
        "name",
        "equipment_type",
        "ip",
        "fqdn",
        "license_end",
        "environment",
    )
    extra = 0


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    form = EquipmentMultipleDocumentationForm
    list_display = (
        "name",
        "equipment_type",
        "ip",
        "fqdn",
        "license_end",
        "environment",
        "get_support_expiration_date",
    )
    list_filter = (
        "license_end",
        "environment",
        "support__expiration_date",
    )
    inlines = (EquipmentDocumentationInline,)
    autocomplete_fields = ("documentation_many",)
    search_fields = (
        "name",
        "ip",
        "ship_to_prod_date",
        "end_of_life",
        "support__expiration_date",
    )

    def get_support_expiration_date(self, obj: Equipment):
        return obj.support.expiration_date if obj.support else datetime.max

    get_support_expiration_date.short_description = _("support expiration")
    get_support_expiration_date.admin_order_field = "support"

    def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None:
        super().save_related(request, form, formsets, change)
        form.save_docs(form.instance)


@admin.register(SSLCert)
class SSLCertAdmin(admin.ModelAdmin):
    list_display = ("name", "expiration_date")
    list_filter = ("expiration_date",)
    list_display = (
        "name",
        "expiration_date",
    )
    search_fields = (
        "name",
        "expiration_date",
    )


@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    form = SoftwareMultipleDocumentationForm
    list_display = ("name", "equipment", "environment")
    list_filter = ("environment", "ship_to_prod_date")
    inlines = (SoftwareDocumentationInline,)
    search_fields = (
        "name",
        "description",
        "environment",
    )

    def save_related(self, request: Any, form: Any, formsets: Any, change: Any) -> None:
        super().save_related(request, form, formsets, change)
        form.save_docs(form.instance)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "phone_number")
    search_fields = (
        "first_name",
        "last_name",
        "poste_occupe",
        "service",
        "division",
        "direction",
    )


@admin.register(SupportContract)
class SupportContractAdmin(admin.ModelAdmin):
    list_display = ("support_provider", "contract_date", "expiration_date")
    list_filter = ("expiration_date", "contract_date")
    search_fields = ("support_provider",)
    # inlines = [EquipmentInline]


@admin.register(DocumentationMany)
class DocumentationAdmin(admin.ModelAdmin):
    list_display = ("documentation",)
    search_fields = ("documentation",)


@admin.register(EquipmentDocumentation)
class DocumentationEquipmentAdmin(admin.ModelAdmin):
    list_display = ("document",)
    search_fields = ("document",)


@admin.register(SoftwareDocumentation)
class DocumentationSoftwareAdmin(admin.ModelAdmin):
    list_display = ("document",)
    search_fields = ("document",)


# Register your models here.
admin.AdminSite.site_header = "ManageIt Administration"
# admin.site.register(Equipment)
# admin.site.register(Software)
# admin.site.register(Person)
# admin.site.register(SupportContract)
# admin.site.register(SSLCert)
