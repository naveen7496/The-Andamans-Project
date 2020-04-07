from django.db import models

class Tribe(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    population = models.IntegerField()
    region = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    existence = models.IntegerField()
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.name
