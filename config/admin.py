from django.contrib import admin

from config.models import Category, SubCategory, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'is_active',
        'created_at'
    ]

    search_fields = [
        'name'
    ]

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'category',
        'is_active',
        'created_at'
    ]

    list_filter = [
        'category',
        'is_active'
    ]

    search_fields = [
        'name'
    ]

    autocomplete_fields = [
        'category'
    ]

    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'created_at'
    ]

    search_fields = [
        'name'
    ]

    prepopulated_fields = {
        'slug': ('name',)
    }