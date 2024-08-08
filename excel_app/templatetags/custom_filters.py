from django import template

register = template.Library()

@register.filter
def get_field_value(obj, field_name):
    """Retrieve the value of a specific field on a model instance."""
    if obj and field_name:
        return getattr(obj, field_name, 'Field not found')
    return 'Invalid object or field name'
