from django.db import models


class Andznakazm(models.Model):
    FirstName = models.CharField(verbose_name='FirstName', max_length=32, blank=False)
    LastName = models.CharField(verbose_name='LastName', max_length=32, blank=False)
    Kochum = models.CharField(verbose_name='kochum', max_length=32, blank=False)