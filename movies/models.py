import uuid
from django.db import models
from datetime import timedelta


class Movie(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=127)
    premiere = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    overview = models.TextField(blank=True, null=True)
    genres = models.ManyToManyField(
        "genres.Genre",
        related_name="movies",
        blank=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        blank=True,
    )
