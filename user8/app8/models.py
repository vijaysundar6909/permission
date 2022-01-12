from django.db import models

# Create your models here.


class emp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  =models.CharField(max_length=100)
    full_name =models.CharField(max_length=100)
    email_id =models.CharField(max_length=100)
    phone_no = models.IntegerField()
    password =models.CharField(max_length=100)
