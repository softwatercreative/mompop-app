from django import forms
from .models import Shops


class ShopsForm(forms.ModelForm):
    class Meta:
        model = Shops
        fields = ['name', 'business_name', 'county', 'type', 'description', 'website']

