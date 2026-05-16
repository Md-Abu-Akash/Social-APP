from django.db import models

from config.common import BaseModel


class Feed(BaseModel):

    FEED_TYPES = (
        ('video', 'Video'),
        ('image', 'Image'),
        ('pdf', 'PDF'),
        ('mixed', 'Mixed'),
    )

    title = models.CharField(
        max_length=500,
        db_index=True
    )

    slug = models.SlugField(
        unique=True,
        db_index=True
    )

    short_description = models.TextField()

    description = models.TextField()

    category = models.ForeignKey(
        'config.Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='feeds',
        db_index=True
    )

    subcategory = models.ForeignKey(
        'config.SubCategory',
        on_delete=models.SET_NULL,
        null=True,
        related_name='feeds',
        db_index=True
    )

    tags = models.ManyToManyField(
        'config.Tag',
        related_name='feeds'
    )

    feed_type = models.CharField(
        max_length=20,
        choices=FEED_TYPES,
        db_index=True
    )

    thumbnail = models.ImageField(
        upload_to='feeds/thumbnails/'
    )

    is_published = models.BooleanField(
        default=False,
        db_index=True
    )

    total_views = models.PositiveBigIntegerField(default=0)

    total_likes = models.PositiveBigIntegerField(default=0)

    total_shares = models.PositiveBigIntegerField(default=0)

    class Meta:
        db_table = 'feeds'

        ordering = ['-created_at']

        indexes = [

            models.Index(fields=['title']),

            models.Index(fields=['feed_type']),

            models.Index(fields=['category']),

            models.Index(fields=['subcategory']),

            models.Index(fields=['is_published']),

            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return self.title



class FeedMedia(BaseModel):

    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('pdf', 'PDF'),
    )

    feed = models.ForeignKey(
        'feeds.Feed',
        on_delete=models.CASCADE,
        related_name='media_files',
        db_index=True
    )

    media_type = models.CharField(
        max_length=20,
        choices=MEDIA_TYPES,
        db_index=True
    )

    file = models.FileField(
        upload_to='feeds/media/'
    )

    thumbnail = models.ImageField(
        upload_to='feeds/media/thumbs/',
        null=True,
        blank=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'feed_media'

        ordering = ['order']

        indexes = [
            models.Index(fields=['feed']),
            models.Index(fields=['media_type']),
        ]



class FeedInternalLink(BaseModel):

    source_feed = models.ForeignKey(
        'feeds.Feed',
        on_delete=models.CASCADE,
        related_name='source_links',
        db_index=True
    )

    target_feed = models.ForeignKey(
        'feeds.Feed',
        on_delete=models.CASCADE,
        related_name='target_links',
        db_index=True
    )

    keyword = models.CharField(
        max_length=255,
        db_index=True
    )

    class Meta:
        db_table = 'feed_internal_links'

        indexes = [
            models.Index(fields=['keyword']),
        ]