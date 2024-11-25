from django.db import models


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
