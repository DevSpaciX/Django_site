from atexit import register
from django import template
from groups.models import Group
import re
register = template.Library()

@register.filter
def word_counter(text):
    formated_text = re.sub(pattern = "[^\w\s]|[\d]", repl = ' ', string = text)
    return f"{text} \n<-- Тут {len(formated_text.split())} слов "


@register.filter
def num_counter(text):
    res = re.findall('(\d+)', text)
    res = [number for number in res if int(number) % 2 == 0]
    if len(res) != 0:
        return f"\n Парные числа - {', '.join(res)} " 
    else:
        return f"\n Парных чисел нет "


@register.inclusion_tag("includes/course_list.html")
def course_by_rating():
    return {
        'object_list':Group.objects.all().order_by("-rating")[:5]
    }