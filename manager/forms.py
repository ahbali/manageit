from manager.models import (
    EquipmentDocumentation,
    Equipment,
    Software,
    SoftwareDocumentation,
)

from django import forms
from django.utils.translation import gettext_lazy as _


class EquipmentMultipleDocumentationForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = ()

    doc_files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add Documentation"),
        required=False,
    )

    def save_docs(self, equipment):
        for file in self.files.getlist("doc_files"):
            doc = EquipmentDocumentation(document=file, model=equipment)
            doc.save()


class SoftwareMultipleDocumentationForm(forms.ModelForm):
    class Meta:
        model = Software
        exclude = ()

    doc_files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add Documentation"),
        required=False,
    )

    def save_docs(self, software):
        for file in self.files.getlist("doc_files"):
            doc = SoftwareDocumentation(document=file, model=software)
            doc.save()
