from django.db import models


class Manufacturer(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    title = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(
            self.manufacturer.title,
            self.title
        )
