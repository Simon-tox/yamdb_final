import datetime

from django.core.validators import MaxValueValidator
from django.db import models

from categories.models import Category
from genres.models import Genre


class Title(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name="titles", null=True)
    genre = models.ManyToManyField(Genre, related_name="titles")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    year = models.IntegerField(validators=
                               [MaxValueValidator
                               (limit_value=datetime.date.today().year)])

    def __str__(self):
        return self.name
