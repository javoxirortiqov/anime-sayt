from django.contrib import admin
from django.utils.html import format_html
from .models import Anime


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = (
        "image_preview",
        "name",
        "janr",
        "yili",
    )

    list_display_links = (
        "name",
    )

    search_fields = (
        "name",
        "izoh",
        "janr",
    )

    list_filter = (
        "janr",
        "yili",
    )

    ordering = (
        "name",
    )

    list_per_page = 20

    def image_preview(self, obj):
        if obj.rasm:
            return format_html(
                '<img src="{}" width="60" height="80" style="border-radius:8px;">',
                obj.rasm.url
            )
        return "-"

    image_preview.short_description = "Poster"