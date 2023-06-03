from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=300)
    author= models.CharField(max_length=200)
    pages=models.IntegerField()
    price=models.FloatField()
    
    def __str__(self):
        return self.title
    