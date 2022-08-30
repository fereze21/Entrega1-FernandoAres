from django.db import models

# Create your models here.
class Author(models.Model):
    nombre= models.CharField(max_length=30)
    DNI= models.IntegerField(primary_key=True)
    telefono=models.IntegerField()
    email = models.EmailField()

class Source(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)
    

class Article(models.Model):
    Author = models.ForeignKey(Author, on_delete=models.SET_NULL,null=True)
    descripcion = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    fuentes = models.ManyToManyField(Source, blank=False)