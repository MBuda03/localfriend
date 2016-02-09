from django.contrib import admin

# Register your models here.
from tours.models import Tour

class TourAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price"]
    search_fields = ["title, description"]
    class Meta:
        model = Tour

admin.site.register(Tour, TourAdmin)
