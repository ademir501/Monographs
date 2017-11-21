from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from website.models import Monograph


class MonographForm(forms.Form):

    class Meta:
        model = Monograph
        fields = '__all__'


class NewMonographForm(ModelForm):

    class Meta:
        model = Monograph
        fields = ['number', 'primary_name', 'secondary_name']

        labels = {
            'number': _('Número'),
            'primary_name': _('Nombre 1'),
            'secondary_name': _('Nombre 2')
        }