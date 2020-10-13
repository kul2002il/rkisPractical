from django.db import models
from django.contrib.auth.models import AbstractUser


class Specialty(models.Model):
    nameRol = models.CharField(max_length=50, verbose_name="name", default='')


class User(AbstractUser):
    fio = models.CharField(max_length=50, verbose_name='ФИО', blank=True)
    role = models.ForeignKey(Specialty, on_delete=models.PROTECT, default=1)

