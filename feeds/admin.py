from django.contrib import admin

from feeds.models import (
    Feed,
    FeedMedia,
    FeedInternalLink
)


class FeedMediaInline(admin.TabularInline):

    model = FeedMedia

    extra = 1


class FeedInternalLinkInline(admin.TabularInline):

    model = FeedInternalLink

    fk_name = 'source_feed'

    extra = 1


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'category',
        'subcategory',
        'feed_type',
        'is_published',
        'created_at'
    ]

    list_filter = [
        'feed_type',
        'category',
        'subcategory',
        'is_published'
    ]

    search_fields = [
        'title',
        'description'
    ]

    autocomplete_fields = [
        'category',
        'subcategory'
    ]

    filter_horizontal = [
        'tags'
    ]

    prepopulated_fields = {
        'slug': ('title',)
    }

    inlines = [
        FeedMediaInline,
        FeedInternalLinkInline
    ]


@admin.register(FeedMedia)
class FeedMediaAdmin(admin.ModelAdmin):

    list_display = [
        'feed',
        'media_type',
        'created_at'
    ]


@admin.register(FeedInternalLink)
class FeedInternalLinkAdmin(admin.ModelAdmin):

    list_display = [
        'source_feed',
        'target_feed',
        'keyword'
    ]