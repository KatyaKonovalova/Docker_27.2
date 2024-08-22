from django.db import models

from config import settings


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )

    preview_course = models.ImageField(
        upload_to="courses/preview_course",
        verbose_name="Превью курса",
        help_text="Загрузите превью(картинку) курса",
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец курса",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Выберите курс",
        blank=True,
        null=True,
    )

    preview_lesson = models.ImageField(
        upload_to="courses/preview_lesson",
        verbose_name="Превью урока",
        help_text="Загрузите превью(картинку) урока",
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
    )

    link_to_video = models.URLField(
        max_length=100,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец урока",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="пользователь",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course, verbose_name="курс в подписке", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
