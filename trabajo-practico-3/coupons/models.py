from django.db import models

# Create your models here.


class Coupon(models.Model):
    name = models.CharField(max_length=255, default='')
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    DISCOUNT_CHOICES = [
        ('5', '5%'),
        ('10', '10%'),
        ('15', '15%'),
        ('25', '25%'),
    ]
    discount = models.CharField(max_length=3, choices=DISCOUNT_CHOICES)
    available = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.name}'
