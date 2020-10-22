from datetime import datetime
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse_lazy


from django.core.validators import RegexValidator


DNSValidator = RegexValidator(
    regex="^[0-9A-Za-z._-]+$",
    message=_(
        "Only alphanumeric characters, hyphens, periods, and underscores are allowed in DNS names"
    ),
    code=_("invalid"),
)


class DocumentationMany(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    documentation = models.FileField(
        upload_to="Documentation/many", null=True, blank=True
    )

    def __str__(self):
        return self.documentation.name


class SupportContract(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    support_provider = models.CharField(
        verbose_name=_("Support provider"), max_length=100, null=True, blank=True
    )
    contract_date = models.DateField(
        verbose_name=_("Contract date"), null=True, blank=True
    )
    expiration_date = models.DateField(
        verbose_name=_("Expiration date"), null=True, blank=True
    )

    class Meta:
        ordering = ["expiration_date"]

    def __str__(self) -> str:
        return f"{self.support_provider}"


class Person(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        verbose_name=_("First name"), max_length=50, null=True, blank=True
    )
    last_name = models.CharField(
        verbose_name=_("Last name"), max_length=50, null=True, blank=True
    )
    poste_occupe = models.CharField(
        verbose_name=_("Position"), max_length=100, null=True, blank=True
    )
    service = models.CharField(
        verbose_name=_("Service"), max_length=100, null=True, blank=True
    )
    division = models.CharField(
        verbose_name=_("Division"), max_length=100, null=True, blank=True
    )
    direction = models.CharField(
        verbose_name=_("Direction"), max_length=100, null=True, blank=True
    )
    phone_number = models.CharField(
        verbose_name=_("Phone number"), max_length=20, null=True, blank=True
    )
    email = models.EmailField(
        verbose_name=_("Email"), max_length=254, null=True, blank=True
    )

    class Meta:
        ordering = ("last_name", "first_name")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class SSLCert(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        verbose_name=_("Name"), max_length=100, null=True, blank=True
    )
    expiration_date = models.DateField(
        verbose_name=_("Expiration date"), null=True, blank=True
    )

    class Meta:
        ordering = ["expiration_date"]

    def __str__(self) -> str:
        return f"{self.name}"


class Equipment(models.Model):
    class TypeOfEquipment(models.TextChoices):
        SERVER = "SRV", _("Server")
        ROUTER = "RTR", _("Router")
        SWITCH = "SW", _("Switch")
        FIREWALL = "FWL", _("Firewall")
        APPLIANCE = "APL", _("Appliance")
        OTHER = "OTHER", _("Other")

    class TypeOfServer(models.TextChoices):
        VIRTUAL = "VIRT", _("Virtual")
        PHYSICAL = "PHYS", _("Physical")

    class TypeOfOS(models.TextChoices):
        WINDOWS = "WIN", _("Windows")
        LINUX = "LINUX", _("Linux")
        BSD = "BSD", _("BSD")
        IOS = "IOS", _("CISCO IOS")
        OTHER = "OTHER", _("Other")

    class TypeOfEnvironment(models.TextChoices):
        PRODUCTION = "PROD", _("Production")
        PRE_PROD = "PRE", _("Pre-production")
        DEVELOPMENT = "DEV", _("Development")

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipment_type = models.CharField(
        verbose_name=_("Equipment type"),
        max_length=5,
        choices=TypeOfEquipment.choices,
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name=_("Name"), max_length=100, null=True, blank=True
    )
    ip = models.GenericIPAddressField(verbose_name=_("IP"), null=True, blank=True)
    fqdn = models.CharField(
        verbose_name=_("FQDN"),
        max_length=1000,
        null=True,
        blank=True,
        validators=[DNSValidator],
    )
    virt_phys = models.CharField(
        verbose_name=_("Virtual/Physical"),
        max_length=4,
        choices=TypeOfServer.choices,
        null=True,
        blank=True,
    )
    operating_system = models.CharField(
        verbose_name=_("Operating system"),
        max_length=5,
        choices=TypeOfOS.choices,
        null=True,
        blank=True,
    )
    support = models.ForeignKey(
        SupportContract,
        verbose_name=_("Support"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    # marche = models.CharField(max_length=200)
    license_end = models.DateField(verbose_name=_("License end"), null=True, blank=True)
    end_of_life = models.DateField(verbose_name=_("End of life"), null=True, blank=True)
    referent_technique = models.ForeignKey(
        Person,
        verbose_name=_("Technical Mentor"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    entite_responsable = models.CharField(
        verbose_name=_("Responsible entity"), max_length=100, null=True, blank=True
    )
    documentation_many = models.ManyToManyField(DocumentationMany, blank=True)
    role = models.CharField(
        verbose_name=_("Role"), max_length=100, null=True, blank=True
    )
    environment = models.CharField(
        verbose_name=_("Environment"),
        max_length=4,
        choices=TypeOfEnvironment.choices,
        null=True,
        blank=True,
    )
    ship_to_prod_date = models.DateField(
        verbose_name=_("Production date"), null=True, blank=True
    )

    class Meta:
        ordering = ["license_end"]

    def get_absolute_url(self):
        return reverse_lazy("manager:equipment-detail", args=[str(self.uid)])

    def __str__(self) -> str:
        return f"{self.name}@{self.ip}"


class Software(models.Model):
    class TypeOfEnvironment(models.TextChoices):
        PRODUCTION = "PROD", _("Production")
        PRE_PROD = "PRE", _("Pre-production")
        DEVELOPMENT = "DEV", _("Development")

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    equipment = models.ForeignKey(
        Equipment,
        verbose_name=_("Equipment"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    referent_technique = models.ForeignKey(
        Person,
        verbose_name=_("Technical Mentor"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name=_("Description"), max_length=1000, null=True, blank=True
    )
    environment = models.CharField(
        verbose_name=_("Environment"),
        max_length=4,
        choices=TypeOfEnvironment.choices,
        null=True,
        blank=True,
    )
    ship_to_prod_date = models.DateField(
        verbose_name=_("Production date"), null=True, blank=True
    )
    database_sever = models.ForeignKey(
        "self",
        verbose_name=_("Database server"),
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-ship_to_prod_date"]

    def __str__(self) -> str:
        return f"{self.name}"


class EquipmentDocumentation(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(
        Equipment, verbose_name=_("Equipment"), on_delete=models.CASCADE
    )
    document = models.FileField(
        verbose_name=_("Document"),
        upload_to="Documentation/equipment",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.document.name


class SoftwareDocumentation(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model = models.ForeignKey(
        Software, verbose_name=_("Software"), on_delete=models.CASCADE
    )
    document = models.FileField(
        verbose_name=_("Document"),
        upload_to="Documentation/software",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.document.name
