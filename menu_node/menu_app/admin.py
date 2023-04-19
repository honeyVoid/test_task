from django.contrib import admin
from menu_app.models import Menu


class MenuAdmin(admin.ModelAdmin):
    """Регистрация модели в  админ-зоне."""
    list_display = ('title', 'url', 'parent')
    list_filter = ('parent',)
    search_fields = ('title', 'url')


admin.site.register(Menu, MenuAdmin)
