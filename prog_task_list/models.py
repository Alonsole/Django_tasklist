from django.db import models


class Tag(models.Model):
    """Модель Тега, содержит имя Тега"""
    name = models.CharField(max_length=100, verbose_name='Имя Тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги/ов'


class Task(models.Model):
    """Создание задачи с обязательными полями “Заголовок”, “Описание”, необязательными полями “Срок”, “Теги”
    (выбираются из списка или добавляются новые), автоматически заполняемыми полями “Выполнено”, “Дата создания”,"""
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=500, verbose_name='Описание')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Срок выполнения')
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True, verbose_name='Теги')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задач'
