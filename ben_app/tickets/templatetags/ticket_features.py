from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def star_replace(count):
    result = ""

    for item in range(0, count):
        result = result + '<i class="fa fa-star"> </i>'

    return mark_safe(result)



