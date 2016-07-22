from django.db import models


class Device(models.Model):
    name = models.CharField('Наименование', max_length=50)
    stream_url = models.CharField('URL путь', max_length=200)

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"
