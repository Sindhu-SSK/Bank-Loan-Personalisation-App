from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Person(models.Model):
    age = models.IntegerField()
    income = models.IntegerField()
    family = models.IntegerField()
    ccavg = models.FloatField()
    education = models.IntegerField()
    mortgage = models.IntegerField()
    personal_loan = models.IntegerField()
    sec_account = models.IntegerField()
    cd_account = models.IntegerField()
    online = models.IntegerField()
    credit_card = models.IntegerField()

    