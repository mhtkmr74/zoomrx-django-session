from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile_number = models.IntegerField(default=None, null=True)
    address = models.TextField()
