from django.db import models
from django.urls import reverse

class Articles(models.Model):
    title = models.CharField('Nagłówek', max_length=50, default='Nazwa artykułu')
    anons = models.CharField('Wstępna część', max_length=250, default='Jakaś część od artykułu')
    full_text = models.TextField('Cały tekst', default='Jakiś text')
    date = models.DateTimeField('Czas tworzenia')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'
