from django.db import models

# Create your models here.
class seller(models.Model):
    name=models.CharField(max_length=50)
    quant=models.IntegerField()
    loc=models.CharField(max_length=50)
    price=models.IntegerField()
    transport=models.CharField(max_length=3)
    tprice=models.IntegerField()
    #image=models.FileField();

class cart(models.Model):
    