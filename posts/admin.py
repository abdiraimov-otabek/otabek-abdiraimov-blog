import markdown
from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.db import models
from django.forms import widgets
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import Post

admin.site.unregister(User)
admin.site.unregister(Group)


@register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):

    list_display = ("name", "id")

    search_fields = ("name",)

    fields = ("name", "permissions")

    list_filter = ("permissions",)

    unfold_settings = {
        "layout": "tabs",
    }

    def save_model(self, request, obj, form, change):
        # Add custom logic before saving the group
        super().save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
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

    class Media:
        css = {"all": ("css/custom_admin.css",)}
