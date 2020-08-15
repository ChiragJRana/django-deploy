from django.db import models

# Create your models here.

class Instruments(models.Model):
    itemname = models.CharField(max_length=100)
    itemvalue = models.IntegerField(default = 0)
    itembool = models.BooleanField(default=False)
    itememail = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.itemname