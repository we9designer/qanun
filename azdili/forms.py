from django import forms
from .models import Azdili

class AzdiliForm(forms.ModelForm):
    class Meta:
        model = Azdili
        fields = [
            'title',
            'description',
            'tags',
        ]