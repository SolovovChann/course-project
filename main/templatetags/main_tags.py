from django import template, templatetags


register = template.Library()


@resister.filter()
def range(min=1):
    return range(min)