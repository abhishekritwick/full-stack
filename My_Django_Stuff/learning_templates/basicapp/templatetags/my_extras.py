from django import template

register = template.Library()

@register.filter(name='cuts')
def cuts(value, arg):
    """
    Cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

@register.filter(name='test2')
def test2(value,arg):
    return "00000"


# register.filter('cuts',cuts)
# register.filter('test2',test2)
