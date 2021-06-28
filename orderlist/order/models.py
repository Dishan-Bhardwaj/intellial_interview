from django.db import models
from datetime import datetime 

# Create your models here.

class customer(models.Model):
    id = models.AutoField (primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact_no = models.CharField(max_length=15)
    pincode = models.IntegerField()


class product(models.Model):
    id = models.AutoField (primary_key=True)
    name = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

class order(models.Model):
    id = models.AutoField (primary_key=True)
    customer_id = models.ForeignKey('customer',on_delete=models.CASCADE)
    product_id = models.ForeignKey('product',on_delete=models.CASCADE) 
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    qty = models.IntegerField()
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    created_date = models.DateTimeField(default=datetime.now)
