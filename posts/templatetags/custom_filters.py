from django import template
import markdown

register = template.Library()


@register.filter
def truncate_markdown(value, length=100):
    # Convert markdown to HTML
    html_content = markdown.markdown(value)

    # Truncate the content and return the first 'length' characters
    return html_content[:length] + ("..." if len(html_content) > length else "")
