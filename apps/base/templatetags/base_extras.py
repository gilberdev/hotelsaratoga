from django import template

register = template.Library()

@register.filter()
def create_range(i):
    return [x for x in range(0,i)]
