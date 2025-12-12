from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.TextField()

    def __str__(self):
        return self.name

class ModelProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    bust = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    hips = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    portfolio_image = models.ImageField(upload_to='portfolios/')

    def __str__(self):
        return self.name
