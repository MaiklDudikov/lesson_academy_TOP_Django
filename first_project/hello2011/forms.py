from django import forms
from .models import Company, Product


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['company', 'name', 'price']
