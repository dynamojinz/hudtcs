from django import template

register = template.Library()

def mul(value, arg):
    """Multiplys the arg to the value."""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except:
            return value

register.filter('mul', mul)
