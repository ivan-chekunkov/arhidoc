from django import forms
from .models import Doc


class DocForm(forms.ModelForm):
    class Meta:
        model = Doc
        fields = (
            "name",
            "number",
            "data_doc",
            "file_doc",
            "category",
        )


class SearcheForm(forms.Form):
    name = forms.CharField(label="Наименование документа", required=False)
    number = forms.CharField(label="Номер документа", required=False)
    data_doc = forms.CharField(label="Дата документа", required=False)
