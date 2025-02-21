from django.db import models

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True) 
    trip_duration = models.DurationField()  
    trip_cost = models.IntegerField() 
    trip_date = models.DateField() 
    trip_passengers = models.IntegerField() 
    trip_boarding = models.CharField(max_length=255) 
    trip_destination = models.CharField(max_length=255)

    def __str__(self):
        return self.trip_destination
