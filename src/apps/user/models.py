from django.contrib.auth.models import AbstractUser
from django.db import models
from django_lifecycle import LifecycleModelMixin
from helpers.models import UUIDModel


class User(LifecycleModelMixin, UUIDModel, AbstractUser):
    post = models.ForeignKey(
        "department.Post", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Должность"
    )
    middle_name = models.CharField("Отчество", max_length=150, blank=True)
    phone = models.CharField("Телефон", max_length=150, blank=True)
    pasport_date = models.DateField("Дата выдачи паспорта", blank=True, null=True)
    pasport_department = models.CharField("Кем выдан паспорт", max_length=150, blank=True)
    pasport_number = models.CharField("Серия и номер паспорта", max_length=150, blank=True)
    date_birth = models.DateField("Дата рождения", blank=True, null=True)
    address = models.CharField("Адрес", max_length=150, blank=True)
    photo = models.ImageField("Фото", upload_to="photo", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name}"

    class Meta(AbstractUser.Meta):
        pass
