from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    number = forms.CharField()

    class Meta:
        model = Document
        fields = (
            "description",
            "document",
        )
