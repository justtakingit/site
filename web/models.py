from django.db import models

# Create your models here.
class message(models.Model):
    time= models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    url= models.CharField(max_length=255)

    def __str__(self):
        return self.title
