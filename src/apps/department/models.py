from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Department(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", null=True, blank=True)
    chief = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Начальник")
    phone = models.CharField("Телефон", max_length=255, null=True, blank=True)
    email = models.EmailField("Электронная почта", null=True, blank=True)
    address = models.CharField("Адрес", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"


class Post(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
