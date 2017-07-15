
from django.template import Library
register=Library()


@register.filter
def judge(value):
    if value == '1':
        return '2'
    else:
        return '1'


