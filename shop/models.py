from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Furniture.Status.Published)


class Furniture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ShopMainView(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    message = models.TextField()

    def __str__(self):
        return self.name