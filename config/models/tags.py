from django.db import models

from ..common import BaseModel


class Tag(BaseModel):

    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True
    )

    slug = models.SlugField(
        unique=True,
        db_index=True
    )

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name