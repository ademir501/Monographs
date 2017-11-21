from django import forms
from website.models import Monograph


class MonographForm(forms.ModelForm):

    class Meta:
        model = Monograph
        fields = '__all__'

        labels = {
            "number": "Número",
            "primary_name": "Nombre uno",
            "secondary_name": "Nombre dos",
        }
