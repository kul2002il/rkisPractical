from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal

from .utilities import send_activation_notification


user_registrated = Signal(providing_args=['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)


class User(AbstractUser):
    fio = models.CharField(max_length=50, verbose_name='Отчество', blank=True)


class Specialty(models.Model):
    nameRol = models.CharField(max_length=50, verbose_name="name", default='')
    userId = models.ForeignKey(User, on_delete=models.PROTECT, default=1)




