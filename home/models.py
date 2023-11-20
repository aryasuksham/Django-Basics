from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null = True, blank = True)
    # image = models.ImageField() #cannot useb ImageField bcoz pillow is not installed, So use command 'pip install pillow'
    file = models.FileField()


class Product(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=150, null=True)


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name


@receiver(post_save, sender = Car)
def call_car_api(sender, instance, **kwargs):
    print("CAR OBJECT CREATED")
    print(sender, instance, kwargs)
