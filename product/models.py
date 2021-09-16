from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.title
