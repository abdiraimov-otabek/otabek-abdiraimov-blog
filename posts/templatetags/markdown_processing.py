from django import template
from django.template.defaultfilters import stringfilter
import markdown

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def convert_markdown(value):
    return markdown.markdown(value)