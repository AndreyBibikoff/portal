from django.db import models
from staff.models import IntebUser

class Clients(models.Model):
    company_name = models.CharField(verbose_name='Название', max_length=128, )
    office_phone = models.PositiveIntegerField(verbose_name='Рабочий телефон')
    office_email = models.EmailField(verbose_name='office_email')
    company_address = models.CharField(verbose_name='Адрес', max_length=64)
    external_ip_v4 = models.CharField(verbose_name='внешний ip', max_length=16, default='0.0.0.0')
    is_active = models.BooleanField(verbose_name='активность', default=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='создан', auto_now=True)

    def __str__(self):
        return self.company_name


class ClientsStaff(models.Model):
    company = models.ForeignKey(Clients, verbose_name='Компания', related_name='company', on_delete=models.CASCADE)
    lastname = models.CharField(verbose_name='Фамилия', max_length=32)
    firstname = models.CharField(verbose_name='Имя', max_length=32)
    middlename = models.CharField(verbose_name='Отчество', max_length=32, blank=True)
    bdate = models.DateField('День рождения', blank=True, null=True)
    position = models.CharField(verbose_name='Должность', max_length=32, blank=True)
    work_phone = models.PositiveIntegerField(verbose_name='рабочий телефон', blank=True)
    mobile_phone = models.PositiveIntegerField(verbose_name='мобильный телефон', blank=True)
    email = models.EmailField(verbose_name='email', blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    is_active = models.BooleanField(verbose_name='активность', default=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='создан', auto_now=True)

def image_folder(self, filename):
    filename = self.company_img.company_name + '.' + filename.split('.')[1]
    return "{0}/{1}".format(self.company_img.company_name, filename)


class Images(models.Model):
    img = models.ImageField(verbose_name='изображение', upload_to=image_folder, blank=True)
    company_img = models.ForeignKey(Clients, related_name='client_images', on_delete=models.CASCADE)


class CompanyComments(models.Model):
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    author = models.ForeignKey(IntebUser, related_name='author', on_delete=models.PROTECT)
    company = models.ForeignKey(Clients, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment