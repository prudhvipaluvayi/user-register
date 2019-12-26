from django.db import models

class employees(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()
    Companyname = models.CharField(max_length=10)
    Age = models.IntegerField()
    City = models.CharField(max_length=10)
    State = models.CharField(max_length=10)
    Zip = models.IntegerField()
    Email = models.CharField(max_length=10)
    Web = models.CharField(max_length=10)


    def __str__(self):
        return self.firstname

# Create your models here.
