from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

val = False

@register.filter
@stringfilter
def value(value):
    val = value
    return val
    

