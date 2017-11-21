from django.http import Http404

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

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


class NewMonographView(CreateView):
    template_name = 'create_monograph.html'
    model = Monograph
    form_class = MonographForm

    def get_context_data(self, **kwargs):
        context = super(NewMonographView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super(NewMonographView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main_page')

    def post(self, request, *args, **kwargs):
        if 'Cancelar' in request.POST:
            return reverse_lazy('main_page')


class UpdateMonographView(UpdateView):
    model = Monograph
    form_class = MonographForm
    template_name = 'edit_monograph.html'

    def get_success_url(self):
        return reverse_lazy('main_page') + "?success=true"


