from django import forms
from website.models import Monograph


class MonographForm(forms.Form):

    class Meta:
        model = Monograph
        fields = '__all__'
