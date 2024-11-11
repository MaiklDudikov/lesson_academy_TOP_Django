from django import forms
from .models import Order


class PersonForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['datetime']
