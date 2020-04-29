from django import forms
from .models import Informatika

class InformatikaForm(forms.ModelForm):
    class Meta:
        model = Informatika
        fields = [
            'title',
            'description',
            'tags',
        ]