from django import template

register = template.Library()

@register.filter
def smart_truncate(value, word_limit=15):
    words = value.split()
    if len(words) <= word_limit:
        return value
    return ' '.join(words[:word_limit]) + '...'
