from django.db import models

# Create your models here.

class History(models.Model):

    tarixiy=models.CharField("Tarixiy", max_length=200)
    zamonaviy=models.CharField("Zamonaviy", max_length=200)

    def __str__(self):
        return self.tarixiy