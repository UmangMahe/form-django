from django.db import models


class Form(models.Model):

    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    
# Create your models here.
