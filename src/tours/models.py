from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.

class Tour(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.title

def tour_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(tour_pre_save_receiver, sender=Tour)
