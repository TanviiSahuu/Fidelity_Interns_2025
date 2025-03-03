from django.db import models

class stocks(models.Model):
    stock_id = models.IntegerField(primary_key=True, editable=True)
    stock_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.stock_id

