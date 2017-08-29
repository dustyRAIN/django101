from django.db import models

# Create your models here.

class appModel(models.Model):

    title = models.CharField(max_length = 120)
    pumba = models.CommaSeparatedIntegerField(max_length = 100)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
