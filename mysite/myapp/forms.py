from django import forms

from myapp.models import Laptop


class LaptopForm(forms.ModelForm):
    class Meta :
        model = Laptop
        fields = ['brand','price','imei','color']