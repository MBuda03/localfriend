from django.db import models

# Create your models here.

class Tour(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


    def __unicode__(self):
        return self.title
