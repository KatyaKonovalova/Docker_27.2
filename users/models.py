from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )

    city = models.CharField(
        verbose_name="Страна",
        max_length=20,
        blank=True,
        null=True,
        help_text="Введите страну проживания",
    )

    avatar = models.ImageField(upload_to="users/avatars/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [("cash", "наличные"), ("card", "банковский перевод")]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )
    payments_date = models.DateTimeField(auto_now=True, verbose_name="дата оплаты")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="оплаченный курс",
        null=True,
        blank=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="оплаченный урок",
        null=True,
        blank=True,
    )
    payment_sum = models.PositiveIntegerField(verbose_name="сумма платежа")
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        default="card",
        verbose_name="способ оплаты",
    )
    payment_link = models.URLField(
        max_length=400, verbose_name="ссылка на оплату", blank=True, null=True
    )
    payment_id = models.CharField(
        max_length=255, verbose_name="идентификатор платежа", blank=True, null=True
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["-payments_date"]  # выбор в обратную сторону (-)
