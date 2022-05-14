from django.db import models


class Url(models.Model):
    objects = models.Manager()
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.link} : {self.uuid}'