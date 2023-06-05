from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=128)
    email=models.EmailField(max_length=64)
    phone=models.IntegerField()
    address=models.CharField(max_length=256)
    salary=models.IntegerField()
    location=models.CharField(max_length=128)
    ceo=models.CharField(max_length=64)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    