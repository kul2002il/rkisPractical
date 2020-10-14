from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fio = models.CharField(max_length=50, verbose_name='Отчество', blank=True)


class Specialty(models.Model):
    nameRol = models.CharField(max_length=50, verbose_name="name", default='')
    userId = models.ForeignKey(User, on_delete=models.PROTECT, default=1)

