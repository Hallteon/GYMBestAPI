from gyms.models import Training, Gym
from django.db import models


class Purchase(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='purchases_training', verbose_name='Тренировка')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='purchases_customer', verbose_name='Покупатель')
    training_price = models.IntegerField(verbose_name='Цена тренировки')
    gym_income = models.IntegerField(verbose_name='Доход зала')

    def __str__(self):
        return f'{self.customer.name} - {self.training_price} руб'

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.CharField(max_length=255, verbose_name='Почта')
    # purchases = models.ManyToManyField('Purchase', related_name='customers_purchase', verbose_name='Покупки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'