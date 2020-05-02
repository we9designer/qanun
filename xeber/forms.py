from django import forms
from .models import Xeber

class XeberForm(forms.ModelForm):
    class Meta:
        model = Xeber
        fields = [
            'title',
            'description',
            'tags',
        ]