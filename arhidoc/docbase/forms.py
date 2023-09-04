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
