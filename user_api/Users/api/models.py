from django.db import models

# Create your models here.
class CustomUser(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email = models.EmailField(('email address'), unique=True)
    company_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    zip = models.IntegerField()
    web = models.CharField(max_length=250)
    age = models.IntegerField()
