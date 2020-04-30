from django import forms
from .models import Mentiq

class MentiqForm(forms.ModelForm):
    class Meta:
        model = Mentiq
        fields = [
            'title',
            'description',
            'tags',
        ]