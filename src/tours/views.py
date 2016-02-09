from django.shortcuts import render

# Create your views here.

# Returns 1 tour with details
def detail_view(request):
    print request
    template = "detail_view.html"
    context = {}
    return render(request, template, context)

# Returns list of tours
def list_view(request):
    print request
    template = "list_view.html"
    context = {}
    return render(request, template, context)
