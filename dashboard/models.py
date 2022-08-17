from django.db import models

# Create your models here.
class addmovie(models.Model):
    title=models.CharField(max_length=100)
    actor=models.CharField(max_length=100)
    trailer=models.CharField(max_length=100)
    poster=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    realeseddate=models.DateField()
    description=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return self.title