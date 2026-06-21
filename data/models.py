from django.db import models


class CarBody(models.Model):
    BODY_TYPE_CHOICES = [
        ('liftback' , 'Liftback'),
        ('sedan' , 'Sedan'),
        ('coupe' , 'Coupe'),
        ('grand_coupe' , 'Grand Coupe'),
        ('crossover' , 'Crossover'),
    ]

    body_type = models.CharField(max_length=100, choices=BODY_TYPE_CHOICES)

    def __str__(self):
        return self.body_type



class Car(CarBody):
    car_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Car Name")
    color = models.CharField(max_length=100, blank=True, null=True, verbose_name="Car Color")
    horsepower = models.IntegerField(blank=True, null=True, verbose_name="Horse Power")
    engine_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Engine Number")
    engine_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Engine Type")
    engine_size = models.CharField(max_length=100, blank=True, null=True, verbose_name="Engine Size")
    manufactured_year = models.IntegerField(blank=True, null=True, verbose_name="Manufactured Year")

    def __str__(self):
        return self.car_name