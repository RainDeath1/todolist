from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    due_date = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
