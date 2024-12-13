from django import template
from apps.product.models import Product
from apps.history.models import OrderHistory, Income


register = template.Library()
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def multiply(value1, value2):
    return value1 * value2

@register.filter
def is_instance_of(obj, class_name):
    if class_name == "OrderHistory" and isinstance(obj, OrderHistory):
        return True
    elif class_name == "Income" and isinstance(obj, Income):
        return True
    return False