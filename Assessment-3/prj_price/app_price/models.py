from django.db import models

# Create your models here.
class Price(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name

