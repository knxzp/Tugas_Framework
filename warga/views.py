from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Warga, Pengaduan
from .forms import WargaForm

class WargaListView(ListView):
    model = Warga
   
class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list') 

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/warga_list.html'
    context_object_name = 'pengaduan_list'