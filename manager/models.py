from datetime import datetime
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class BaseType(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    installation_date = models.DateTimeField(default=timezone.now)
    expected_lifetime = models.DurationField()
    expiration_date = models.DateTimeField(default=timezone.now)

    @property
    def computed_expiration_date(self):
        return self.installation_date + self.expected_lifetime

    class Meta:
        abstract = True


class Hardware(BaseType):
    class TypeOfHardware(models.TextChoices):
        SERVER = "SRV", _("Server")
        ROUTER = "RTR", _("Router")
        SWITCH = "SW", _("Switch")
        FIREWALL = "FWL", _("Firewall")
        WORKSTATION = "WS", _("Work Station")

    hardware_type = models.CharField(
        max_length=4, choices=TypeOfHardware.choices, default=TypeOfHardware.SERVER,
    )


class Software(BaseType):
    class TypeOfSoftware(models.TextChoices):
        OS = "OS", _("Operating System")
        ANTIVIRUS = "AV", _("AntiVirus")
        EMAIL_SERVER = "MAIL", _("Email Server")

    software_type = models.CharField(
        max_length=4, choices=TypeOfSoftware.choices, default=TypeOfSoftware.OS,
    )

