from django import template

register=template.library()

@register.simple_tag
def find_len(user):
    return 
