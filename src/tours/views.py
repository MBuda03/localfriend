from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from localfriend.mixins import MultiSlugMixin

from tours.forms import TourAddForm, TourModelForm
from tours.models import Tour
from django.utils.text import slugify

# Create your views here.

class TourCreateView(CreateView):
    model = Tour
    template_name = "form_include.html"
    form_class = TourModelForm

    #Need to change this later
    success_url = "/tours/add/"

    def get_context_data(self, *args, **kwargs):
        context = super(TourCreateView, self).get_context_data(*args, **kwargs)
        context["submit_btn"] = "Create Tour"
        return context

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(TourCreateView, self).form_valid(form)
        return valid_data

class TourUpdateView(MultiSlugMixin, UpdateView):
    model = Tour
    template_name = "form_include.html"
    form_class = TourModelForm

    #Need to change this later
    success_url = "/tours/"

    def get_context_data(self, *args, **kwargs):
        context = super(TourUpdateView, self).get_context_data(*args, **kwargs)
        context["submit_btn"] = "Update Tour"
        return context

    def get_object(self, *args, **kwargs):
        user = self.request.user
        obj = super(TourUpdateView, self).get_object(*args, **kwargs)
        if obj.user == user or user in obj.managers.all():
            return obj
        else:
            raise Http404

class TourListView(ListView):
    model = Tour

    def get_queryset(self, *args, **kwargs):
        qs = super(TourListView, self).get_queryset(**kwargs)
        return qs

class TourDetailView(MultiSlugMixin, DetailView):
    model = Tour


def create_view(request):
    form = TourModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

    template = "create_view.html"
    context = {
        "form":form,
    }
    return render(request, template, context)

# Edit a tour
def update_view(request, object_id=None):
    tour = get_object_or_404(Tour, id=object_id)
    form = TourModelForm(request.POST or None, instance=tour)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
    template = "update_view.html"
    context = {
        "object": tour,
        "form": form,
        }
    return render(request, template, context)


# Returns 1 tour with details
def detail_view(request, object_id=None):
    tour = get_object_or_404(Tour, id=object_id)
    template = "detail_view.html"
    context = {
        "object": tour
        }
    return render(request, template, context)

# Returns 1 tour with details
def detail_slug_view(request, slug=None):
    tour = get_object_or_404(Tour, slug=slug)
    template = "detail_view.html"
    context = {
        "object": tour
        }
    return render(request, template, context)


# Returns list of tours
def list_view(request):
    print request
    template = "list_view.html"
    context = {}
    return render(request, template, context)
