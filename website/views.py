from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from website.forms import MonographForm
from website.models import Monograph


class MainView(ListView):
    template_name = 'monograph_list_template.html'
    model = Monograph

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['monographs'] = Monograph.objects.all()
        context['is_success'] = self.request.GET.get('success', False)
        return context


class NewMonographView(ListView):
    template_name = 'monograph_list_template.html'
    model = Monograph

    def get_context_data(self, **kwargs):
        context = super(NewMonographView, self).get_context_data(**kwargs)
        context['monographs'] = Monograph.objects.all()
        return context


class UpdateMonographView(UpdateView):
    model = Monograph
    form_class = MonographForm
    template_name = 'edit_monograph.html'

    def get_success_url(self):
        return reverse_lazy('main_page') + "?success=true"


