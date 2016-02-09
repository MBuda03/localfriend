from django.http import Http404
from django.shortcuts import render, get_object_or_404

from tours.forms import TourAddForm, TourModelForm
from tours.models import Tour
from django.utils.text import slugify

# Create your views here.

def create_view(request):
    form = TourModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.slug = slugify(instance.title)
        instance.save()

    """
    if form.is_valid():
        data = form.cleaned_data
        title = data.get("title")
        description = data.get("description")
        price = data.get("price")
        new_obj = Tour()
        new_obj.title = title
        new_obj.description = description
        new_obj.price = price
        new_obj.save()
    """


    template = "create_view.html"
    context = {
        "form":form,
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
