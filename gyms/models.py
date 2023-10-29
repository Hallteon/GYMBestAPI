from django.db import models


class Training(models.Model):
    training_type = models.CharField(max_length=255, verbose_name='Тип тренировки')
    price = models.IntegerField(verbose_name='Цена')
    gym = models.ForeignKey('Gym', on_delete=models.CASCADE, related_name='trainings_gym', verbose_name='Зал')

    def __str__(self):
        return f'{self.gym.gym_name} - {self.training_type} - {self.price} руб'

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'


class Gym(models.Model):
    gym_name = models.CharField(max_length=255, verbose_name='Название филиала зала')
    administrator_name = models.CharField(max_length=255, verbose_name='Имя администратора')
    administrator_phone = models.CharField(max_length=50, verbose_name='Телефон администратора')
    # trainings = models.ManyToManyField('Training', blank=True, related_name='gyms_training', verbose_name='Тренировки')
    free_slots = models.IntegerField(verbose_name='Количество свободных слотов для записи')

    def __str__(self):
        return self.gym_name

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

