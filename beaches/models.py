from django.db import models


class Beach(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name
