from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from website.forms import MonographForm, NewMonographForm
from website.models import Monograph


class MainView(ListView):
    template_name = 'monograph_list_template.html'
    model = Monograph

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['monographs'] = Monograph.objects.all()
        return context


class NewMonographView(CreateView):
    template_name = 'create_monograph.html'
    model = Monograph
    form_class = NewMonographForm

    def get_context_data(self, **kwargs):
        context = super(NewMonographView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        number = form.data['number']
        primary_name = form.data['primary_name']
        secondary_name = form.data['secondary_name']
        try:
            monograph = Monograph.objects.create(number=number, primary_name=primary_name, secondary_name=secondary_name)
        except:
            raise Http404
        return reverse_lazy('main_page')


class UpdateMonographView(UpdateView):
    model = Monograph
    form_class = MonographForm
    template_name = 'edit_monograph.html'

