from django.db import models


# Create your models here.
class BackForm(models.Model):
    name = models.CharField(max_length=300, verbose_name='Имя клиента')
    phone = models.CharField(max_length=300, verbose_name='Телефон клиента')
    email = models.CharField(max_length=1000, verbose_name='Почта клиента')

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'

    def __str__(self):
        return 'Клиент: ' + 'Имя: ' + self.name + ' Телефон: ' + self.phone
