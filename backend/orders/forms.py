from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model  = Order
        fields = ['shipping_address', 'city', 'postal_code', 'phone']
        labels = {
            'shipping_address': 'Adresse de livraison',
            'city':             'Ville',
            'postal_code':      'Code postal',
            'phone':            'Téléphone',
        }
        widgets = {
            'shipping_address': forms.Textarea(attrs={'rows': 3}),
        }
