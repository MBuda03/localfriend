from django.db import models

# Create your models here.

class Tour(models.Model):
    title = models.CharField()

    def __unicode__(self):
        return self.title
