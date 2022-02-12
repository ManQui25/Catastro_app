from django.db import models

# Create your models here.

class Owner(models.Model):
    TYPE_PROP = (
        ('Persona Natural', 'Persona Natural'),
        ('Persona Jurídica', 'Persona Jurídica')
    )
    document = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    type_p= models.CharField(max_length=200, null=True, choices=TYPE_PROP)

class Predio(models.Model):
    CATEGORY = (
			('Urbano', 'Urbano'),
			('Rural', 'Rural'),
			) 
            
    document = models.IntegerField(primary_key=True)
    matricula = models.IntegerField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    Location = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ManyToManyField('Owner', related_name='predios', blank=True)

