from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    
    def __str__(self):
        return f'{self.name} - {self.price}'