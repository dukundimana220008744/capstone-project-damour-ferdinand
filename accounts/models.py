from django.db import models

# Create your models here.

class user_tbl(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    reg_date = models.DateField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.fname

    
