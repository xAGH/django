from django.db import models


# Create your models here.
table = lambda name: 'hola\".\"' + name\

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    
    class Meta():
        managed = False
        db_table = table('tasks')