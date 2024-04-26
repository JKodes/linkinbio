from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    model = Link
    
class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy('links-list')
    
class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('links-list')
    
class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('links-list')
    


