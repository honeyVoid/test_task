from django.db import models


class Menu(models.Model):
    """Древовидная модель для Меню."""
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'self', null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title[:30]
