# my_portfolio/main/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter
def range_filter(value):
    return range(value)
