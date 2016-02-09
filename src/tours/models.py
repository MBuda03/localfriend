from django.db import models

# Create your models here.

class Tour(models.Model):
    title = models.CharField(max_length=140)

    def __unicode__(self):
        return self.title
