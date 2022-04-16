from django.forms import ModelForm
from django.forms import ModelForm, TextInput, NumberInput
from .models import Widget


class WidgetsForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']
        widgets = {
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'Description'}),
            'quantity': NumberInput(attrs={'quantity': 'number', 'placeholder': '0'})
        }
