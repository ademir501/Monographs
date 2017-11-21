from django import forms
from website.models import Monograph


class MonographForm(forms.ModelForm):

    class Meta:
        model = Monograph
        fields = '__all__'
