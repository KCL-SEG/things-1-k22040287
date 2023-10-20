from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        validators = [RegexValidator(
            regex = r'^([0-9]|[1-9][0-9]|100)$',
            message = 'Quantity must be a number',
            code = 'invalid_quantity'
        )]
    )
    
