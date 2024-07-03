from django.db import models

# Create your models here.
class Vehicle(models.Model):
    user_name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=13)
    vehicle_type = models.CharField(max_length=10)
    brand = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    year_of_purchase = models.DateField()
    kilometers = models.IntegerField()
    color = models.CharField(max_length=20)
    registered_state = models.CharField(max_length=20)
    num_of_oweners = models.IntegerField()
    payment_mode = models.CharField(max_length=20)
    


