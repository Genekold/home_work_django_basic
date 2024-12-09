from django.db import models

from users.models import User


class Blog(models.Model):
    """Модель объекта Blog"""

    BOOLEAN_FIELD = [
        (True, 'Опубликован'),
        (False, 'Не опубликован')
    ]

    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок блога",
        help_text="Введите заголовок",
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Текст блога",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="blogs/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью блога",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        auto_now_add=True
    )
    is_active = models.BooleanField(
        verbose_name="Признак публикации ",
        choices=BOOLEAN_FIELD,
        default=False
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Введите количество просмотров",
        default=0
    )
    creator = models.ForeignKey(
        User,
        verbose_name='Автор статьи',
        help_text='Укажиете автора статьи',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        permissions = [
            ("can_unpublish_blog", "can unpublish blog",)
        ]


class Autor(models.Model):
    autor = models.ForeignKey(
        Blog,
        related_name='autor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Автор статьи'
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя автора",
        help_text="Введите имя автора",
        blank=True,
        null=True,
        default=None
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия автора",
        help_text="Введите фамилию автора",
        blank=True,
        null=True,
        default=None
    )

