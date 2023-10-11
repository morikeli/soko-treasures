from django import template

register = template.Library()

@register.filter
def totalcost(price, quantity):
    return price * quantity