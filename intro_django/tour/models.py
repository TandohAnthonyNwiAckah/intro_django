from django.db import models

# Create your models here.

class Tour(models.Model):
    # Origin country, destination, tour price.
     origin_country = models.CharField(max_length=64)
     destination_country  = models.CharField(max_length=64)
     number_of_nights = models.IntegerField()
     price = models.IntegerField()

     # this a string representation of the Tour
     def __str__(self):
        return(f"ID {self.id}: From {self.origin_country} To {self.destination_country} will cost {self.price}")