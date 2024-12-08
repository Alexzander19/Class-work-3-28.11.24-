from django.db import models

# Create your models here.

class Auto_new(models.Model):
    mark = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    we_are_by = models.IntegerField()
    price = models.IntegerField()
    picture = models.ImageField(upload_to='img/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return f'{self.mark}: {self.model}'

