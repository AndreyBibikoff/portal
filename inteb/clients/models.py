from django.db import models


class Clients(models.Model):
    company_name = models.CharField(verbose_name='Name', max_length=128, )
    office_phone = models.PositiveIntegerField(verbose_name='Рабочий телефон')
    office_email = models.EmailField(verbose_name='office_email')
    company_address = models.CharField(verbose_name='Адрес', max_length=32)

    def __str__(self):
        return self.company_name


class ClientsStaff(models.Model):
    company = models.ForeignKey(Clients, related_name='company', on_delete=models.CASCADE)
    lastname = models.CharField(verbose_name='Фамилия', max_length=32)
    firstname = models.CharField(verbose_name='Имя', max_length=32)
    middlename = models.CharField(verbose_name='Отчество', max_length=32, blank=True)
    bdate = models.DateField('День рождения',  blank=True, null=True)
    position = models.CharField(verbose_name='Должность', max_length=32, blank=True)
    work_phone = models.PositiveIntegerField(verbose_name='рабочий телефон', blank=True)
    mobile_phone = models.PositiveIntegerField(verbose_name='мобильный телефон', blank=True)
    email = models.EmailField(verbose_name='email', blank=True)


def image_folder(self, filename):
    filename = self.company_img.company_name + '.' + filename.split('.')[1]
    return "{0}/{1}".format(self.company_img.company_name, filename)


class Images(models.Model):
    img = models.ImageField(verbose_name='изображение', upload_to=image_folder, blank=True)
    company_img = models.ForeignKey(Clients, related_name='client_images', on_delete=models.CASCADE)
