from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import markdown
from django.utils.safestring import mark_safe
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_desc = models.CharField(max_length=255, default="No Description Provided!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Auto-generate slug if it is empty
        if not self.slug:
            self.slug = slugify(self.title)  # Convert the title to a slug format
        super().save(*args, **kwargs)

    def render_markdown(self):
        """Render Markdown content to HTML."""
        md = markdown.Markdown(
            extensions=[
                "markdown.extensions.fenced_code",
                "markdown.extensions.tables",
                "markdown.extensions.nl2br",
                "markdown.extensions.codehilite",
            ]
        )
        return mark_safe(md.convert(self.content))

    def __str__(self):
        return self.title
