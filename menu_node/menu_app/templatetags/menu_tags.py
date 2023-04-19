from django import template
from django.urls import reverse

from menu_app.models import Menu


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path
    menu_items = Menu.objects.filter(title=menu_name)
    return get_menu_html(menu_items, current_url)


def get_menu_html(menu_items, current_url):
    menu_html = '<ul>'
    for item in menu_items:
        if item.url and (
            item.url == current_url or current_url.startswith(item.url)
        ):
            active_class = 'active'
        else:
            active_class = ''
        menu_html += '<li class="{}"><a href="{}">{}</a>'.format(
            active_class, get_url(item), item.title
        )
        if item.children.exists():
            menu_html += get_menu_html(item.children.all(), current_url)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html


def get_url(menu_item):
    if menu_item.url:
        return menu_item.url
    elif menu_item.named_url:
        return reverse(menu_item.named_url)
    else:
        return ''
