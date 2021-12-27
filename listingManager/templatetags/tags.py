from django import template

register = template.Library()

@register.filter
def dash_for_none(val):
    if val != '':
        return val
    return '-'