from django.db import models

class Island(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    distance = models.IntegerField()
    area = models.CharField(max_length=200)
    population = models.IntegerField()
    highest_elevation = models.DecimalField(max_digits=3, decimal_places=2)
    coastline = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.name
