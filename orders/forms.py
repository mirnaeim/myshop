from django import forms
from .models import Order
from localflavor.ir.forms import IRPostalCodeField


class OrderCreateForm(forms.ModelForm):
    postal_code = IRPostalCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                'postal_code', 'city']
