from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm
from rest_framework.generics import ListAPIView
from .serializers import WargaSerializer

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

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' 
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')

class WargaListAPIView(ListAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
