from django.http import Http404
from django.shortcuts import render, get_object_or_404

from tours.models import Tour

# Create your views here.

# Returns 1 tour with details
def detail_view(request, object_id=None):
    tour = get_object_or_404(Tour, id=object_id)
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
