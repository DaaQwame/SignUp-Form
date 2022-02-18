from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.

class Form(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Date_of_birth = models.DateField()
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=10)
    Password = models.CharField(max_length=256)

    def verify_password(raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
