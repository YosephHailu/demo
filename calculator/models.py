from django.db import models

# Create your models here.


class CalculatorHistory(models.Model):
    expression = models.CharField(max_length=200)
    result = models.FloatField()