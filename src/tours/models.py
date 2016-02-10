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

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug

    qs = Tour.objects.filter(slug=slug).exists()
    if qs:
        new_slug = "%s-%s" %(slug, instance.id)
        create_slug(instance, new_slug=new_slug)
    return slug

def tour_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(tour_pre_save_receiver, sender=Tour)
