from django.db import models


class Device(models.Model):
    PROTOCOLS= (
        ('rtsp', 'rtsp'),
        ('http', 'http'),
        ('rtp', 'rtp'),
    )

    name = models.CharField('Наименование', max_length=50)
    protocol = models.CharField('Протокол', max_length=5, default=PROTOCOLS[0][0], choices=PROTOCOLS)
    mac = models.CharField('Mac адрес', max_length=17, default='deadbeeffordad')
    ip = models.GenericIPAddressField('IP адрес', protocol='both', unpack_ipv4=True, default='127.0.0.1')
    stream_url = models.CharField('URL путь', max_length=200)
    status = models.BooleanField('Статус', default=False)

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    def __str__(self):
        return '{0} -> {1}'.format(self.name, self.stream_url)