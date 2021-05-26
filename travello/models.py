from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField()
    desc = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name