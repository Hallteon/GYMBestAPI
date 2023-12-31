# Generated by Django 4.2.6 on 2023-10-21 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym_name', models.CharField(max_length=255, verbose_name='Название филиала зала')),
                ('administrator_name', models.CharField(max_length=255, verbose_name='Имя администратора')),
                ('administrator_phone', models.CharField(max_length=50, verbose_name='Телефон администратора')),
                ('free_slots', models.IntegerField(verbose_name='Количество свободных слотов для записи')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_type', models.CharField(max_length=255, verbose_name='Тип тренировки')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings_gym', to='gyms.gym', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Тренировка',
                'verbose_name_plural': 'Тренировки',
            },
        ),
        migrations.AddField(
            model_name='gym',
            name='trainings',
            field=models.ManyToManyField(related_name='gyms_training', to='gyms.training', verbose_name='Тренировки'),
        ),
    ]
