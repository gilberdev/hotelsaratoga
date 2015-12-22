from django import template
import re

register = template.Library()


@register.filter()
def create_range(i):
    return [x for x in range(0, i)]


@register.filter()
def customize_date(d):
    a = d.strftime('%B %d, %Y, %H:%M%p')
    print(d)
    print(a)
    return a


@register.filter()
def first_paragraph(text):
    first_paragraph = re.split('\s{4,}', text)[0]
    return first_paragraph
