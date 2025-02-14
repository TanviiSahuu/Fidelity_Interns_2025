from django.db import models

# Create your models here.
class school(models.Model):
    schl_id = models.IntegerField(primary_key=True)
    schl_name = models.CharField(max_length=100)
    schl_add = models.CharField(max_length=100)
    schl_fees = models.IntegerField()

    def __str__(self):
        return self.schl_name
