from django import template
from django.utils.safestring import mark_safe

from calcu.forms import WeirdCalcuForm

register = template.Library()


@register.inclusion_tag('calcu/calcu_form.html')
def weird_calcu_form():
    return {'form': WeirdCalcuForm}

@register.simple_tag
def weird_calcu_answer():
    return mark_safe('<div id="WeirdCalcu_answer"></div>')
