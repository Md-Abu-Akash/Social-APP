from django.db import models

from ..common import BaseModel


class Category(BaseModel):

    name = models.CharField(
        max_length=255,
        unique=True,
        db_index=True
    )

    slug = models.SlugField(
        unique=True,
        db_index=True
    )

    icon = models.ImageField(
        upload_to='categories/icons/',
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'categories'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.name


class SubCategory(BaseModel):

    category = models.ForeignKey(
        'config.Category',
        on_delete=models.CASCADE,
        related_name='subcategories',
        db_index=True
    )

    name = models.CharField(
        max_length=255,
        db_index=True
    )

    slug = models.SlugField(
        unique=True,
        db_index=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'subcategories'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name