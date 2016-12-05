from django import template
from django.utils.safestring import mark_safe # to prevent django
                                              # auto escaping
import markdown

register = template.Library()

from ..models import Post

@register.simple_tag
def total_posts():
    """ tags to return total number of published
        posts
    """
    return Post.published.count()

@register.filter(name='markdown')
def markdown_format(text):
    """ retuen markdowned version of text """
    return mark_safe(markdown.markdown(text))
