from django import template

register = template.Library()

@register.filter
def is_librarian(user):
    if not user.is_authenticated:
        return False
    return user.is_staff or user.groups.filter(name="Librarians").exists()
