
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class IntebUser(AbstractUser):
    birthday = models.DateField(verbose_name='день рождения', default='1900-01-01')
    avatar = models.ImageField(verbose_name='картинка', upload_to='media/avatars', blank=True)
    middle_name = models.CharField(verbose_name='отчество', max_length=150, blank=True)
    create = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    update = models.DateTimeField(verbose_name='обновлен', auto_now_add=True)