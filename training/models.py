from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

User = get_user_model()

class TrainingProgram(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Статус')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    class Meta:
        verbose_name = 'Тренировочная программа'
        verbose_name_plural = 'Тренировочные программы'

    def __str__(self):
        return self.name[:50]

    def get_absolute_url(self):
        return reverse('training_program_details', args=[self.pk])

class TrainingDay(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    order_num = models.SmallIntegerField(verbose_name='Сортировка')
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE, related_name='training_days')

    class Meta:
        verbose_name = 'Тренировочный день'
        verbose_name_plural = 'Тренировочные дни'

    def __str__(self):
        return self.name[:50]

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.name[:50]

class TrainingExercise(models.Model):
    order_num = models.SmallIntegerField()
    training_day = models.ForeignKey(TrainingDay, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Упражнение в трерировке'
        verbose_name_plural = 'Упражнения в тренировках'


class Set(models.Model):
    weight = models.FloatField()
    reps = models.SmallIntegerField()
    rest_seconds = models.SmallIntegerField()
    order_num = models.SmallIntegerField()
    training_exercise = models.ForeignKey(TrainingExercise, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Подход'
        verbose_name_plural = 'Подходы'