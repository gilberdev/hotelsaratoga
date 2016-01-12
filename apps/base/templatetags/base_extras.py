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

@register.filter()
def rest_items(l):
    return l[1:]

@register.filter()
def first_item(l):
    return l[0]

@register.filter()
def first_item_background(l):
    return l[0].image.url

@register.filter()
def first_item_name(l):
    return l[0].name

@register.filter()
def first_item_description(l):
    return l[0].description

@register.filter()
def return_item(d,i):
    return d[i]