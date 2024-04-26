from django.shortcuts import get_object_or_404, render
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
    


def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context ={
        'profile' : profile,
        'links' : links
    }
    return render(request, 'linksrepo/profile.html', context )