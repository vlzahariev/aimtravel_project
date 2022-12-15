from django.db import models
from model_utils import Choices

from aimtravel_project.web.validators import max_value


class JobOffer(models.Model):
    job_position = models.CharField(
        verbose_name='Позиция',
        max_length=30,
        blank=True,
        null=True,
    )
    employer = models.CharField(
        verbose_name='Работодател',
        max_length=30,
        blank=True,
        null=True,
    )
    wage = models.FloatField(
        verbose_name='Заплащане',
        blank=True,
        null=True,
    )
    city = models.CharField(
        verbose_name='Град',
        max_length=20,
        blank=True,
        null=True,
    )
    state = models.CharField(
        verbose_name='Щат',
        max_length=20,
        blank=True,
        null=True,
    )
    sponsor = models.CharField(
        verbose_name='Спонсор',
        max_length=15,
        blank=True,
        null=True,
    )
    offer_pic = models.URLField(
        verbose_name='Снимка-URL',
        blank=True,
        null=True,
    )
    job_description = models.TextField(
        blank=True,
        null=True,
    )
    ranking = models.PositiveIntegerField(
        validators=(max_value,),
        default=1,
        blank=True,
        null=True,
    )

    def __str__(self):
        result = f'{self.job_position} at {self.employer} - {self.city}, {self.state}'
        return result


class Prices(models.Model):
    PRICING_TYPE = Choices('Self Arranged', 'Full Placement Standard', 'Premium Full Placement', )
    DEFAULT_PRICING_TYPE = 'Full Placement Standard'

    pricing_type = models.CharField(
        verbose_name='Ценови план:',
        max_length=25,
        default=DEFAULT_PRICING_TYPE,
        choices=PRICING_TYPE,
        blank=True,
        null=True,
    )

    price = models.FloatField(
        verbose_name='Цена:',
    )

    price_description = models.TextField(
        verbose_name='В цената е включено:',
        blank=True,
        null=True,
        help_text="Моля добавете описание",
    )

    def __str__(self):
        return f"{self.pricing_type}: $ {self.price:.2f}"


class AdditionalServices(models.Model):
    service_type = models.CharField(
        verbose_name='Вид услуга',
        max_length=30,
        blank=True,
        null=True,
    )
    service_description = models.TextField(
        verbose_name='Описание на услугата',
        blank=True,
        null=True,
    )
    service_price = models.FloatField(
        verbose_name='Цена на услугата',
        blank=True,
        null=True,
    )


class Company(models.Model):
    employer_name = models.CharField(
        verbose_name="Работодател",
        max_length=25,
        blank=False,
        null=True,
    )
    employer_city = models.CharField(
        verbose_name='Град',
        max_length=15,
        blank=False,
        null=True,
    )
    employer_state = models.CharField(
        verbose_name='Щат',
        max_length=2,
        blank=False,
        null=True,
    )
    employer_history = models.TextField(
        verbose_name='Кратка история',
        max_length=250,
        blank=False,
        null=True,
    )
    employer_photo = models.URLField(
        verbose_name='Снимка-URL',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.employer_name}'
