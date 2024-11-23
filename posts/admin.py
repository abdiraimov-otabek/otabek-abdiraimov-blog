from django.contrib import admin
from django.db import models
from django.forms import widgets
from django.utils.safestring import mark_safe
import markdown
from .models import Post
from django.contrib.admin import ModelAdmin


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ["title", "slug", "created_at", "published", "short_desc"]
    search_fields = ["title", "content"]
    list_filter = ["published", "created_at"]
    readonly_fields = [
        "content_preview",
        "slug",
    ]  # Make slug readonly as it's auto-generated

    formfield_overrides = {
        models.TextField: {
            "widget": widgets.Textarea(
                attrs={
                    "rows": 20,
                    "class": "vLargeTextField",
                }
            )
        },
    }

    def content_preview(self, obj):
        """Render the Markdown content to HTML"""
        if obj.content:
            md = markdown.Markdown(
                extensions=[
                    "markdown.extensions.fenced_code",
                    "markdown.extensions.tables",
                    "markdown.extensions.nl2br",
                    "markdown.extensions.codehilite",  # For code syntax highlighting
                ]
            )
            return mark_safe(md.convert(obj.content))
        return "No content provided."

    content_preview.short_description = "Markdown Preview"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "author",
                    "content",
                    "short_desc",
                    "published",
                )
            },
        ),
        (
            "Preview",
            {
                "fields": ("content_preview",),
                "classes": ("collapse",),
                "description": "This shows a live preview of the rendered Markdown content.",
            },
        ),
    )
