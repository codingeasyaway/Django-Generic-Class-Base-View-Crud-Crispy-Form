from django.shortcuts import render
from .models import Candidate
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
# (R) READ
class Read(ListView):
    template_name = 'list.html'
    model = Candidate
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_candidate = Candidate.objects.all().order_by("-id")
        context['all_candidate'] = all_candidate
        return context
# (C) CREATE
class Create(CreateView):
    template_name = 'form.html'
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')

# (U) UPDATE
class Update(UpdateView):
    template_name = 'form.html'
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')
# (D) DELETE
class Delete(DeleteView):
    model = Candidate
    success_url = reverse_lazy('read')
    template_name = 'delete.html'

