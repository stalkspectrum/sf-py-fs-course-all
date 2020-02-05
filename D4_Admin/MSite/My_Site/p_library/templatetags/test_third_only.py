from django.template.library import Library

register = Library()

@register.filter
def only3rd(value):
    if (int(value) % 3) == 0:
        return True
    return False
