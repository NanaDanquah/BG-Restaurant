from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[
                                MinValueValidator(5.00)])
    inventory = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.title}'
