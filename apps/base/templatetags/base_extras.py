from django import template

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
